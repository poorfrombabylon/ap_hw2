from config import TOKEN
from aiogram import Bot, Dispatcher
from middleware import LoggingMiddleware
from api import setup_handlers
import asyncio

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Настраиваем middleware и обработчики
dp.message.middleware(LoggingMiddleware())
setup_handlers(dp)


async def main():
    print("Бот запущен!")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
