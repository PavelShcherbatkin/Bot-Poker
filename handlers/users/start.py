from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    text = [
        f'Привет, {message.from_user.full_name}!',
        'Для получения полного функционала вам необходимо зарегистрироваться /reg',
        'Для получения справки по коммандам введите комманду /help'
    ]
    await message.answer('\n'.join(text))