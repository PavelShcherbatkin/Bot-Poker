from aiogram import types

from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext

from loader import dp
from states.add import Add
from states.sub import Sub

from .sql import DBCommands
database = DBCommands()


async def f(x):
    result = ''
    for line in x:
        result += line[0] + ': ' + str(line[1]) + '\n'
    return result


#Диспатчер для reg
@dp.message_handler(Command('reg'))
async def check_balance_all(message: types.Message):
    check = await database.check_user()
    if check == False:
        await database.reg()
        balance = await database.check_money()
        text = [
            'Регистрация прошла успешно',
            f'Сейчас у вас на счету {balance} монет',
            'Для проверки баланса введите команду /balance',
            'Для получения справки введите /help'
            ]
        await message.answer('\n'.join(text))
    else:
        await message.answer('Вы уже зарегистрированы')

#Диспатчеры для пополнения счета
@dp.message_handler(Command('add'), state=None)
async def run_add(message: types.Message):
    check = await database.check_user() 
    if check == True:
        await message.answer('Введите сумму для пополнения')
        await Add.Q1.set()
    else:
        await message.answer('Пожалуйста зарегистрируйтесь /reg')

@dp.message_handler(state=Add.Q1)
async def add_money(message: types.Message, state: FSMContext):
    answer = abs(int(message.text))
    await database.add_money(answer)
    balance = await database.check_money()
    text = [
        f'Вы внесли {answer} монет',
        f'Сейчас у вас на счету {balance} монет',
        'Для проверки баланса введите команду /balance'
    ]
    await message.answer('\n'.join(text))
    await state.finish()


#Диспатчеры для снятия со счета
@dp.message_handler(Command('sub'), state=None)
async def run_sub(message: types.Message):
    check = await database.check_user() 
    if check == True:
        await message.answer('Введите сумму для снятия')
        await Sub.Q1.set()
    else:
        await message.answer('Пожалуйста зарегистрируйтесь /reg')

@dp.message_handler(state=Sub.Q1)
async def sub_money(message: types.Message, state: FSMContext):
    answer = abs(int(message.text))
    await database.sub_money(answer)
    balance = await database.check_money()
    text = [
        f'Вы сняли {answer} монет',
        f'Сейчас у вас на счету {balance} монет',
        'Для проверки баланса введите команду /balance'
    ]
    await message.answer('\n'.join(text))
    await state.finish()


#Диспатчер для balance
@dp.message_handler(Command('balance'))
async def check_balance(message: types.Message):
    check = await database.check_user()
    if check == True:
        balance = await database.check_money()
        await message.answer(f'Сейчас у вас на счету {balance} монет')
    else:
        await message.answer('Пожалуйста зарегистрируйтесь /reg')


#Диспатчер для all
@dp.message_handler(Command('all'))
async def check_balance_all(message: types.Message):
    check = await database.check_user()
    if check == True:
        money_all = await database.check_money_all()
        text = await f(money_all)
        await message.answer(text)
    else:
        await message.answer('Пожалуйста зарегистрируйтесь /reg')