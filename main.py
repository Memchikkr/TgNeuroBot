import asyncio
import logging

from aiohttp import BasicAuth
from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession
from aiohttp_socks import ProxyConnector, ProxyType

from config import project_settings
from src.handlers.start import router as start_router
from src.handlers.chatgpt import router as chat_gpt_router

# auth = BasicAuth(login=project_settings.proxy_login, password=project_settings.proxy_password)
# session = AiohttpSession(proxy=(project_settings.proxy_url))
bot = Bot(token=project_settings.tg_token)
dp = Dispatcher()

async def main():
    dp.include_router(start_router)
    dp.include_router(chat_gpt_router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
