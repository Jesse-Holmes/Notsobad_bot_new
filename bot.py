import asyncio
import openai
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import Command

API_TOKEN = '8015977055:AAEzOQMzc3wH-aXh-d5wXDZtpBUlfcRNzQY'
OPENAI_API_KEY = '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'

openai.api_key = OPENAI_API_KEY

bot = Bot(
    token=API_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher()

@dp.message(Command("start"))
async def send_welcome(message: Message):
    await message.answer("Привет! Я твой личный GPT-помощник 🤖")

@dp.message()
async def gpt_chat(message: Message):
    await message.chat.do("typing")
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # или "gpt-4", если у тебя есть доступ
            messages=[
                {"role": "user", "content": message.text}
            ]
        )
        answer = response["choices"][0]["message"]["content"]
        await message.answer(answer.strip())
    except Exception as e:
        await message.answer(f"Ошибка: {str(e)}")

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
