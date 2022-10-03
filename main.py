from aiogram import Bot, Dispatcher, executor, types
import json

f = open('.credentials.json')
CREDENTIALS = json.load(f)
bot = Bot(token=CREDENTIALS["TELEGRAM_TOKEN"])
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI am Nure Schedule bot!")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
