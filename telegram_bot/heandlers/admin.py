from aiogram.dispatcher import FSMContext
from aiogram import types
from aiogram.dispatcher.filters.state import State, StatesGroup
from create_bot import dp, bot

class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()


#Начало диалога загрузки нового продукта в меню
@dp.message_handler(commands=('Загрузить'), state=None)
async def cm_start(message : types.Message):
    await FSMAdmin.photo.set()
    await message.reply('Загрузить фото')
