import os
import asyncio
from aiohttp import web
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

API_TOKEN = os.environ.get("BOT_TOKEN")
if not API_TOKEN:
    raise RuntimeError("BOT_TOKEN is not set")

PORT = int(os.environ.get("PORT", 10000))

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

async def handle_root(request):
    return web.Response(text="Bot is running!")

@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("Бот запущен ✅")

async def start_polling():
    await dp.start_polling(bot, handle_signals=False)

async def start_app():
    app = web.Application()
    app.add_routes([web.get("/", handle_root)])
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", PORT)
    await site.start()
    print(f"Server running on port {PORT}")
    await start_polling()

if __name__ == "__main__":
    asyncio.run(start_app())

