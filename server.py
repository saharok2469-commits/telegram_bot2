import os
import asyncio
from flask import Flask
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

# Загружаем данные окружения
API_TOKEN = os.environ.get("BOT_TOKEN")
GROUP_CHAT_ID = "-1003376710670"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Flask сервер
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

# Telegram bot handlers
@dp.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer("Привет! Бот работает 😊")

async def start_bot():
    await dp.start_polling(bot)

if __name__ == "__main__":
    # Запускаем aiogram в фоне
    loop = asyncio.get_event_loop()
    loop.create_task(start_bot())

    # Запускаем Flask (это важно для Render!)
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
