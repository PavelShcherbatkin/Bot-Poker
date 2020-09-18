import sqlite3

from aiogram import types

from check_db import path_to_db

class DBCommands:
    path = path_to_db
    CHECK_USER = "SELECT * FROM users WHERE my_id=?"
    ADD_NEW_USER = 'INSERT INTO users (my_id, first_name, second_name, account) values(?, ?, ?, ?)'
    ADD_MONEY = 'UPDATE users SET account=account+? WHERE my_id=?'
    SUB_MONEY = 'UPDATE users SET account=account-? WHERE my_id=?'
    CHECK_MONEY = "SELECT account FROM users WHERE my_id=?"
    CHECK_MONEY_ALL = "SELECT first_name, account FROM users"


    async def check_user(self):
        command = self.CHECK_USER
        user = types.User.get_current()
        my_id = int(user.id)
        result = None
        try:
            conn = sqlite3.connect(self.path)
            result = conn.execute(command, (my_id,)).fetchall()
        except:
            print('Возникла ошибка в check_user')
        finally:
            conn.close()
        if result:
            return True
        else:
            return False


    async def reg(self):
        command = self.ADD_NEW_USER
        user = types.User.get_current()
        my_id = int(user.id)
        first_name = user.first_name
        second_name = user.last_name
        balance = 0
        try:
            conn = sqlite3.connect(self.path)
            conn.execute(command, (my_id, first_name, second_name, balance))
            conn.commit()
        except:
            print('Возникла ошибка в reg')
        finally:
            conn.close()


    async def add_money(self, money):
        command = self.ADD_MONEY
        user = types.User.get_current()
        my_id = int(user.id)
        try:
            conn = sqlite3.connect(self.path)
            conn.execute(command, (money, my_id))
            conn.commit()
        except:
            print('Возникла ошибка в add_money')
        finally:
            conn.close()


    async def sub_money(self, money):
        command = self.SUB_MONEY
        user = types.User.get_current()
        my_id = int(user.id)
        try:
            conn = sqlite3.connect(self.path)
            conn.execute(command, (money, my_id))
            conn.commit()
        except:
            print('Возникла ошибка в sub_money')
        finally:
            conn.close()


    async def check_money(self):
        command = self.CHECK_MONEY
        user = types.User.get_current()
        my_id = int(user.id)
        try:
            conn = sqlite3.connect(self.path)
            result = conn.execute(command, (my_id,)).fetchall()[0][0]
        except:
            print('Возникла ошибка в check_money')
        finally:
            conn.close()
        return result

    
    async def check_money_all(self):
        command = self.CHECK_MONEY_ALL
        try:
            conn = sqlite3.connect(self.path)
            result = conn.execute(command).fetchall()
        except:
            print('Возникла ошибка в check_money_all')
        finally:
            conn.close()
        return result