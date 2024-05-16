from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


neural_networks = [{'name': 'ChatGPT', 'callback': 'chatgpt'}]

async def neural_network_kb():
    keyboard = InlineKeyboardBuilder()
    for neural in neural_networks:
        keyboard.add(InlineKeyboardButton(text=neural['name'], callback_data=neural['callback']))
    return keyboard.adjust(2).as_markup()
