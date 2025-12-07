import os
from flask import Flask, request
from aiogram import Bot, Dispatcher, types
import asyncio

TOKEN = os.environ.get("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher()

app = Flask(__name__)

@app.get("/")
def home():
    return "Webhook bot running!"

@app.post("/webhook")
def webhook():
    update = types.Update.model_validate(request.json)
    asyncio.get_event_loop().create_task(dp.feed_update(bot, update))
    return ""

@dp.message()
async def start(msg: types.Message):
    await msg.answer("Бот работает через Webhook! 😊")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
