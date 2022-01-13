from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram import executor
from config import TOKEN

import os, json, string

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

async def on_startup(_):
    print('Бот вышел в онлайн')

#|Админ часть|

#|Польз. Часть|

@dp.message_handler(commands=['start','help'])
async def command_start(msg: types.Message):
    try:
        await bot.send_message(msg.from_user.id, 'Приятного аппетита')
        await msg.delete()
    except:
        await msg.reply('Общение с ботом через Лс, напишите ему')

@dp.message_handler(commands=['График_роботы'])
async def pizza_open_command(msg: types.Message):
    await bot.send_message(msg.from_user.id,'Мы никогда не работаем. Так как наша компания обанкротилась.')

@dp.message_handler(commands=['Расположение'])
async def pizza_place_command(msg: types.Message):
    await bot.send_message(msg.from_user.id, 'Улица пушкина дом колотушкина')
#|Общая Часть|

@dp.message_handler()
async def echo_send(msg: types.Message):
    if {i.lower().translate(str.maketrans('','', string.punctuation))for i in msg.text.split(' ')}\
        .intersection(set(json.load(open('bad_words.json')))) != set():
        await msg.reply('Маты запрещенны!')
        await msg.delete()



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)