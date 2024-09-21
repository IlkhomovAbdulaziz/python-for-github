from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

API_TOKEN = '7492485473:AAGbG9wgTFkHx8HU547XauYAPK-JbWjcLus'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    button1 = KeyboardButton('Sherik kerak')
    button2 = KeyboardButton('Hodim kerak')
    button3 = KeyboardButton('Ish joyi kerak')
    button4 = KeyboardButton('Ustoz kerak')
    button5 = KeyboardButton('Shogird kerak')
    markup.add(button1, button2, button3, button4, button5)
    await message.reply("Iltimos, amalni tanlang:", reply_markup=markup)


@dp.message_handler(lambda message: message.text == 'Sherik kerak')
async def process_action1(message: types.Message):
    data = """
Sherik topish uchun ariza berish

Hozir sizga birnecha savollar beriladi. 
Har biriga javob bering. 
Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.
"""
    await message.reply(data)
    await message.answer("Ism Familiyangizni kiriting")


@dp.message_handler(lambda message: message.text == 'Amal 2')
async def process_action2(message: types.Message):
    await message.reply("Siz Amal 2 ni tanladingiz.")


@dp.message_handler(lambda message: message.text == 'Amal 3')
async def process_action3(message: types.Message):
    await message.reply("Siz Amal 3 ni tanladingiz.")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)