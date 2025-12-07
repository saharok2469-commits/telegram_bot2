import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

API_TOKEN = os.environ["BOT_TOKEN"]

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer("Бот работает! 😊")

async def main():
    print("Bot started...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
