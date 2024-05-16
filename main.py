from aiogram import Bot, Dispatcher
import asyncio
from config.config import BOT_TOKEN
from handlers.handlers import router
async def main():
    bot = Bot(token=BOT_TOKEN)
    dispatcher = Dispatcher()

    dispatcher.include_routers(router)
    await dispatcher.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        exit()