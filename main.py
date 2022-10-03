from aiogram import Bot, Dispatcher, executor, types
import json

f = open('.credentials.json')
CREDENTIALS = json.load(f)
bot = Bot(token=CREDENTIALS["TELEGRAM_TOKEN"])
dp = Dispatcher(bot)

users = {}


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    users[message.from_user.id] = ''
    await bot.send_message(message.from_user.id, "Hi!\nI am Nure Schedule bot! Введіть назву групи українькою:")


@dp.message_handler(commands=['check'])
async def get_group(message: types.Message):
    await bot.send_message(message.from_user.id, f"Група {users[message.from_user.id]}")


@dp.message_handler(commands=['change'])
async def set_group(message: types.Message):
    users[message.from_user.id] = ''
    await bot.send_message(message.from_user.id, "Введіть нову назву групи українькою:")


@dp.message_handler()
async def send_welcome(message: types.Message):
    user_id = message.from_user.id
    if users[user_id] == '':
        users[user_id] = message.text.upper()
        await bot.send_message(user_id, f"Group has been set as {users[user_id]}")
    else:
        await bot.send_message(user_id, "Групу вже обрано. Для зміни введіть /change")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
