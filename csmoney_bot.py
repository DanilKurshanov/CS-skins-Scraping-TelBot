from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import hbold, hlink

from main import collect_data

import asyncio
import json
import os
import time

bot = Bot(token=os.getenv('TOKEN'), parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    start_buttons = ['🔪 Knives', '🧤 Gloves', '🧨 Sniper Rifles']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)

    await message.answer('Secect a category', reply_markup=keyboard)

@dp.message_handler(Text(equals='🔪 Knives'))
async def get_discount_knives(message: types.Message):
    await message.answer('Loading... Please waiting')

    collect_data(category_type=2)

    with open('result.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    for index, item in enumerate(data):
        card = f'{hlink(item.get("full_name"), item.get("3d"))}\n' \
            f'{hbold("Discount: ")}{item.get("overprice")}%\n' \
            f'{hbold("Price: ")}{item.get("item_price")}$\n'

        if index%20 == 0:
            await asyncio.sleep(3)

        await message.answer(card)

@dp.message_handler(Text(equals='🧤 Gloves'))
async def get_discount_guns(message: types.Message):
    await message.answer('Loading... Please waiting')

    collect_data(category_type=13)

    with open('result.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    for index, item in enumerate(data):
        card = f'{hlink(item.get("full_name"), item.get("3d"))}\n' \
            f'{hbold("Discount: ")}{item.get("overprice")}%\n' \
            f'{hbold("Price: ")}{item.get("item_price")}$\n'

        if index%20 == 0:
            await asyncio.sleep(3)

        await message.answer(card)


@dp.message_handler(Text(equals='🧨 Sniper Rifles'))
async def get_discount_guns(message: types.Message):
    await message.answer('Loading... Please waiting')

    collect_data(category_type=4)

    with open('result.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    for index, item in enumerate(data):
        card = f'{hlink(item.get("full_name"), item.get("3d"))}\n' \
            f'{hbold("Discount: ")}{item.get("overprice")}%\n' \
            f'{hbold("Price: ")}{item.get("item_price")}$\n'

        if index%20 == 0:
            await asyncio.sleep(3)

        await message.answer(card)


def main():
    executor.start_polling(dp)

if __name__ == '__main__':
    main()