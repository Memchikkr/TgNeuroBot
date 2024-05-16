from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from src.service.chatgpt import ChatGptService


router = Router(name='ChatGPT')

class ChattingState(StatesGroup):
    message = State()


@router.callback_query(F.data == 'chatgpt')
async def start_chat_gpt(callback: CallbackQuery, state: FSMContext):
    await callback.answer('Success')
    await state.set_state(ChattingState.message)
    await callback.message.answer(text="Welcome to ChatGPT")
    
    

@router.message(ChattingState.message)
async def message_to_chat_gpt(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(ChattingState.message)
    answer = await ChatGptService.get_answer(message=message)
    await message.answer(answer)

@router.message(F.text == 'Exit')
async def exit_chat_gpt(message: Message, state: FSMContext):
    await message.answer('Exit!')
    await state.clear()
