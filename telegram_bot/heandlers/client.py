from aiogram import types, Dispatcher
from create_bot import dp, bot
from keybords import kb_client

#@dp.message_handler(commands=['start','help'])
async def command_start(msg: types.Message):
    try:
        await bot.send_message(msg.from_user.id, 'Приятного аппетита', reply_markup=kb_client)
        await msg.delete()
    except:
        await msg.reply('Общение с ботом через Лс, напишите ему')

#@dp.message_handler(commands=['График_роботы'])
async def pizza_open_command(msg: types.Message):
    await bot.send_message(msg.from_user.id,'Мы никогда не работаем. Так как наша компания обанкротилась.')

#@dp.message_handler(commands=['Расположение'])
async def pizza_place_command(msg: types.Message):
    await bot.send_message(msg.from_user.id, 'Улица пушкина дом колотушкина')

def register_heandlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start','help'])
    dp.register_message_handler(pizza_open_command, commands=['График_роботы'])
    dp.register_message_handler(pizza_place_command, commands=['Расположение'])