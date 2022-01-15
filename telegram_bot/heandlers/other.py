from aiogram import types,Dispatcher
import json, string
from create_bot import dp, bot

#@dp.message_handler()
async def echo_send(msg: types.Message):
    if {i.lower().translate(str.maketrans('','', string.punctuation))for i in msg.text.split(' ')}\
        .intersection(set(json.load(open('bad_words.json')))) != set():
        await msg.reply('Маты запрещенны!')
        await msg.delete()

def register_heandlers_other(dp : Dispatcher):
    dp.register_message_handler(echo_send)
