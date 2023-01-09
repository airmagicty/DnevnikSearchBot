import re
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from CONFIG import *

bot = Bot(API_TOKEN)
dp = Dispatcher(bot)

def call_back_return():
    print("Hello!")
def test_menu() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True,
                             one_time_keyboard=True)
    kb1 = KeyboardButton("Авт1")
    kb2 = KeyboardButton("Авт2")
    kb3 = KeyboardButton("/help")
    return kb.add(kb1).insert(kb2).add(kb3)

def test_imenu() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(row_width=2)
    ikb1 = InlineKeyboardButton(text="Test1",
                                url="https://google.com")
    ikb2 = InlineKeyboardButton(text="Test2",
                                url="https://google.com")
    ikb3 = InlineKeyboardButton(text="Test3",
                                callback_data="summon_test")
    return ikb.add(ikb1, ikb2).add(ikb3)

async def on_bot_start(_):
    print("I started")

@dp.message_handler(commands=['menu'])
async def echo_menu(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="Menu",
                           reply_markup=test_imenu()
                           )

@dp.message_handler(commands=['img'])
async def echo_img(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo=IMG_URL)

@dp.message_handler(commands=['sticker'])
async def echo_sticker(message: types.Message):
    await bot.send_sticker(chat_id=message.from_user.id,
                           sticker='CAACAgIAAxkBAAEHKgZjubMISJ0NWmCOascFkOue0MngegACcAEAAs6YzRbDY97SastfMC0E',
                           reply_markup=ReplyKeyboardRemove())

@dp.message_handler(commands=['start','restart'])
async def echo_start(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="Test",
                           parse_mode='HTML',
                           reply_markup=test_menu())

@dp.message_handler(commands=['help'])
async def echo_help(message: types.Message):
    await message.reply(text=HELP_LIST, parse_mode='MarkdownV2')

if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           skip_updates=True,
                           on_startup=on_bot_start)