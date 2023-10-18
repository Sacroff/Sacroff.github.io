from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo
import json

bot = Bot('6084999549:AAGHiUobAlyhAjIG8oiE2nr2aDweaD7G61g')
dp = Dispatcher(bot)


@dp.message_handler(commands=['starts'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открыть веб страницу', web_app=WebAppInfo(url='https://itproger.com/telegram.html')))
    await message.answer('Привет, мой друг!', reply_markup=markup)


@dp.message_handler(content_types=['web_app_data'])
async def web_app(message: types.Message):
    res = json.loads(message.web_app_data.data)
    await message.answer(f'Name: {res["name"]}. Email: {res["email"]}. Phone: {res["phone"]}')


executor.start_polling(dp)
