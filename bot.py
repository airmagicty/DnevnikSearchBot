import re
import random
from aiogram import Bot, Dispatcher, executor, types
from CONFIG import *

bot = Bot(API_TOKEN)
dp = Dispatcher(bot)

alfavit = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

@dp.message_handler()
async def echo(message: types.Message):
    await bot.send_sticker(message.from_user.id, sticker='CAACAgIAAxkBAAEHKgZjubMISJ0NWmCOascFkOue0MngegACcAEAAs6YzRbDY97SastfMC0E')

@dp.message_handler(commands=['start','restart'])
async def echo_start(message: types.Message):
    await message.answer(text=message.text)

@dp.message_handler(commands=['help'])
async def echo_help(message: types.Message):
    await message.reply(text=HELP_LIST, parse_mode='MarkdownV2')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)