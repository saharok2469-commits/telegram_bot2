# server.py
import os
import asyncio
from aiohttp import web
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

API_TOKEN = os.environ.get("BOT_TOKEN")
if not API_TOKEN:
    raise RuntimeError("BOT_TOKEN is not set in environment variables")

PORT = int(os.environ.get("PORT", 10000))

bot = Bot(token=API_TOKEN)
dp = Dispatcher()


# HTTP handler для Render — он проверит, что порт открыт
async def handle_root(request):
    return web.Response(text="Bot is running!")

# Телеграм-обработчик /start
@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer("Привет! Бот работает ✅")

async def start_polling():
    # handle_signals=False чтобы избежать ошибок set_wakeup_fd в средах типа Render
    await dp.start_polling(bot, handle_signals=False)

async def start_app():
    # создаём aiohttp-приложение и запускаем его на PORT
    app = web.Application()
    app.add_routes([web.get("/", handle_root)])

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", PORT)
    await site.start()
    print(f"HTTP server started on port {PORT}")

    # запускаем polling — это будет работать в том же event loop
    await start_polling()

if __name__ == "__main__":
    # запускаем всё в asyncio.run — этот процесс будет держать порт открытым
    asyncio.run(start_app())
