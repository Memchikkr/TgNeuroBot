from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


neural_networks = [{'name': 'Replicate', 'callback': 'replicate'}]

async def neural_network_kb():
    keyboard = InlineKeyboardBuilder()
    for neural in neural_networks:
        keyboard.add(InlineKeyboardButton(text=neural['name'], callback_data=neural['callback']))
    return keyboard.adjust(2).as_markup()


replicate_mods = [
    {'name': 'Create', 'callback': "create"},
    {'name': 'Edit', 'callback': "edit"}
]
async def replicate_mods_kb():
    keyboard = InlineKeyboardBuilder()
    for mode in replicate_mods:
        keyboard.add(InlineKeyboardButton(text=mode['name'], callback_data=mode['callback']))
    return keyboard.adjust(2).as_markup()


replicate_create_models = [
    {'name': 'RealvisXL', 'callback': "replicate_create&realvisxl"}
]

replicate_edit_models = [
    {'name': 'RemBg', 'callback': "replicate_edit&rembg"}
]

async def replicate_create_kb():
    keyboard = InlineKeyboardBuilder()
    for model in replicate_create_models:
        keyboard.add(InlineKeyboardButton(text=model['name'], callback_data=model['callback']))
    return keyboard.adjust(2).as_markup()

async def replicate_edit_kb():
    keyboard = InlineKeyboardBuilder()
    for model in replicate_edit_models:
        keyboard.add(InlineKeyboardButton(text=model['name'], callback_data=model['callback']))
    return keyboard.adjust(2).as_markup()
