from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from src.keyboards.reply import start
from src.keyboards.inline import neural_network_kb


router = Router(name='Start')

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Hello!', reply_markup=start)

@router.message(F.text == 'Menu')
async def menu(message: Message):
    await message.answer(text='Select a neural network', reply_markup=await neural_network_kb())
