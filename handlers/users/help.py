from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp
from utils.misc import rate_limit


@rate_limit(5, 'help')
@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = [
        'Список команд: ',
        '/reg - Регистрация',
        '/add - Пополнить счет',
        '/sub - Снять со счета',
        '/balance - Проверить баланс',
        '/all - Проверить баланс всех кто есть в базе',
        '/help - Получить справку'
    ]
    await message.answer('\n'.join(text))
