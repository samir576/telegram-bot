import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message

# 🔑 Сюда вставь свой токен от BotFather
TOKEN = "сюда_вставь_твой_токен"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message()
async def echo(message: Message):
    await message.answer("Привет! Я твой бот 😊")

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
