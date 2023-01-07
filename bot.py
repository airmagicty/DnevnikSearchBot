import re
import random
from aiogram import Bot, Dispatcher, executor, types
from CONFIG import *

bot = Bot(API_TOKEN)
dp = Dispatcher(bot)

def create_menu():
    return 0

@dp.message_handler(commands=['img'])
async def echo_img(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id, photo=IMG_URL)

@dp.message_handler(commands=['locate'])
async def echo_locate(message: types.Message):
    await bot.send_location(message.from_user.id)

@dp.message_handler(commands=['sticker'])
async def echo_sticker(message: types.Message):
    await bot.send_sticker(message.from_user.id, sticker='CAACAgIAAxkBAAEHKgZjubMISJ0NWmCOascFkOue0MngegACcAEAAs6YzRbDY97SastfMC0E')

@dp.message_handler(commands=['start','restart'])
async def echo_start(message: types.Message):
    await message.answer(text=message.text)
    await message.delete()

@dp.message_handler(commands=['help'])
async def echo_help(message: types.Message):
    await message.reply(text=HELP_LIST, parse_mode='MarkdownV2')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)