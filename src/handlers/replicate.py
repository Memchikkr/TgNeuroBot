from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import MagicData
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

import src.keyboards.inline as inline_kb
from src.service.replicate import ReplicateService

router = Router(name='Replicate')

class CreateState(StatesGroup):
    ref = State()
    width = State()
    height = State()
    prompt = State()

class EditState(StatesGroup):
    ref = State()
    image = State()


@router.callback_query(F.data == 'replicate')
async def start_replicate(callback: CallbackQuery):
    await callback.answer('Success')
    await callback.message.edit_text(text="Welcome to Replicate, enter the mode", reply_markup=await inline_kb.replicate_mods_kb())

@router.callback_query((F.data == 'create') | (F.data == 'edit'))
async def entering_mode(callback: CallbackQuery):
    await callback.answer('Success')
    if callback.data == 'create':
        reply_markup = await inline_kb.replicate_create_kb()
    elif callback.data == 'edit':
        reply_markup = await inline_kb.replicate_edit_kb()
    await callback.message.edit_text(text="Enter the model", reply_markup=reply_markup)

@router.callback_query(F.data.startswith('replicate_create&'))
async def start_creating(callback: CallbackQuery, state: FSMContext):
    await callback.answer('Success')
    await state.update_data(ref=callback.data.split('&')[1])
    await state.set_state(CreateState.width)
    await callback.message.answer(text="Enter the width")

@router.message(CreateState.width)
async def enter_width(message: Message, state: FSMContext):
    if int(message.text) % 16 != 0:
        await message.answer(text='Try again, the number should be completely divisible by 16')
        return
    await state.update_data(width=int(message.text))
    await state.set_state(CreateState.height)
    await message.answer(text="Enter the height")

@router.message(CreateState.height)
async def enter_height(message: Message, state: FSMContext):
    if int(message.text) % 16 != 0:
        await message.answer(text='Try again, the number should be completely divisible by 16')
        return
    await state.update_data(height=int(message.text))
    await state.set_state(CreateState.prompt)
    await message.answer(text="Enter the prompt")

@router.message(CreateState.prompt)
async def enter_height(message: Message, state: FSMContext):
    await state.update_data(prompt=message.text)
    data = await state.get_data()
    result = await ReplicateService.get_answer(data)
    await message.answer_photo(photo=result, caption='Your photo is ready!')
    await state.clear()

@router.callback_query(F.data.startswith('replicate_edit&'))
async def start_editing(callback: CallbackQuery, state: FSMContext):
    await callback.answer('Success')
    await state.update_data(ref=callback.data.split('&')[1])
    await state.set_state(EditState.image)
    await callback.message.answer(text="Enter the image url")

@router.message(EditState.image)
async def enter_image_url(message: Message, state: FSMContext):
    await state.update_data(image=message.text)
    data = await state.get_data()
    result = await ReplicateService.get_answer(data)
    await message.answer(text=result)
    await state.clear()
