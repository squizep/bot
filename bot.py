import sqlite3

import telebot
from telebot import types

import config

# BOT
bot = telebot.TeleBot(config.TOKEN)

user = None
text123 = None


@bot.message_handler(commands=['start'])
def start(message):
    global user
    user = message.from_user.id
    if user in config.USER:
        # DATA BASE
        db = sqlite3.connect('server.db')
        cursor = db.cursor()
        cursor.execute(
            """ CREATE TABLE IF NOT EXISTS login_id (user_id INTEGER PRIMARY KEY) """)
        cursor.execute(
            """ CREATE TABLE IF NOT EXISTS lecture (id INTEGER PRIMARY KEY AUTOINCREMENT, NERV TEXT, OFT TEXT, PED TEXT, AG TEXT, FH TEXT, FT TEXT, fk_login_id INTEGER REFERENCES login_id(user_id) ) """)
        cursor.execute(
            f""" INSERT INTO lecture(fk_login_id) VALUES({user}) """)
        db.commit()

        # Добавляю telegram id user в DATA BASE
        people_id = user
        cursor.execute(f"DELETE FROM login_id WHERE user_id = {people_id}")
        data = cursor.fetchone()

        if data is None:
            user_id = [user]
            cursor.execute("INSERT INTO login_id(user_id) VALUES(?);", user_id)
            db.commit()
        else:
            pass

        person1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Н,Г')
        item2 = types.KeyboardButton('ОФТ')
        item3 = types.KeyboardButton('ПЕД')
        item4 = types.KeyboardButton('АГ')
        item5 = types.KeyboardButton('ФХ')
        item6 = types.KeyboardButton('ФТ')
        item7 = types.KeyboardButton('Все предметы')
        person1.add(item1, item2, item3, item4, item5, item6, item7)
        bot.send_message(message.chat.id, '...', reply_markup=person1)

    else:
        bot.send_message(message.chat.id, 'нет доступа')


@bot.message_handler(func=lambda message: message.text == 'Н,Г')
def lecture_NERV(message):
    db = sqlite3.connect('server.db')
    cursor = db.cursor()
    global user
    user = message.from_user.id
    global text123
    text123 = "NERV"
    if user in config.USER:
        qwe = cursor.execute(
            f" SELECT lecture.NERV FROM lecture WHERE lecture.fk_login_id = {user}")
        db.commit()
        button = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item = types.KeyboardButton('поставить НБ')
        item1 = types.KeyboardButton('В начало')
        button.add(item, item1)
        bot.send_message(message.chat.id, qwe, reply_markup=button)
    else:
        bot.send_message(message.chat.id, 'нет доступа')


@bot.message_handler(func=lambda message: message.text == 'ФХ')
def lecture_FH(message):
    db = sqlite3.connect('server.db')
    cursor = db.cursor()
    global user
    global text123
    text123 = "FH"
    user = message.from_user.id
    if user in config.USER:
        qwe = cursor.execute(
            f" SELECT lecture.FH FROM lecture WHERE lecture.fk_login_id = {user}")
        db.commit()
        button = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item = types.KeyboardButton('поставить НБ')
        item1 = types.KeyboardButton('В начало')
        button.add(item, item1)
        bot.send_message(message.chat.id, qwe, reply_markup=button)
    else:
        bot.send_message(message.chat.id, 'нет доступа')


@bot.message_handler(func=lambda message: message.text == 'АГ')
def lecture_AG(message):
    db = sqlite3.connect('server.db')
    cursor = db.cursor()
    global user
    global text123
    user = message.from_user.id
    text123 = 'AG'
    if user in config.USER:
        qwe = cursor.execute(
            f" SELECT lecture.AG FROM lecture WHERE lecture.fk_login_id = {user}")
        db.commit()
        button = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item = types.KeyboardButton('поставить НБ')
        item1 = types.KeyboardButton('В начало')
        button.add(item, item1)
        bot.send_message(message.chat.id, qwe, reply_markup=button)
    else:
        bot.send_message(message.chat.id, 'нет доступа')


@bot.message_handler(func=lambda message: message.text == 'ПЕД')
def lecture_PED(message):
    db = sqlite3.connect('server.db')
    cursor = db.cursor()
    global user
    global text123
    user = message.from_user.id
    text123 = "PED"
    if user in config.USER:
        qwe = cursor.execute(
            f" SELECT lecture.PED FROM lecture WHERE lecture.fk_login_id = {user}")
        db.commit()
        button = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item = types.KeyboardButton('поставить НБ')
        item1 = types.KeyboardButton('В начало')
        button.add(item, item1)
        bot.send_message(message.chat.id, qwe, reply_markup=button)
    else:
        bot.send_message(message.chat.id, 'нет доступа')


@bot.message_handler(func=lambda message: message.text == 'ОФТ')
def lecture_OFT(message):
    db = sqlite3.connect('server.db')
    cursor = db.cursor()
    global user
    global text123
    user = message.from_user.id
    text123 = "OFT"
    if user in config.USER:
        qwe = cursor.execute(
            f" SELECT lecture.OFT FROM lecture WHERE lecture.fk_login_id = {user}")
        db.commit()
        button = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item = types.KeyboardButton('поставить НБ')
        item1 = types.KeyboardButton('В начало')
        button.add(item, item1)
        bot.send_message(message.chat.id, qwe, reply_markup=button)
    else:
        bot.send_message(message.chat.id, 'нет доступа')


@bot.message_handler(func=lambda message: message.text == 'ФТ')
def lecture_FT(message):
    db = sqlite3.connect('server.db')
    cursor = db.cursor()
    global user
    global text123
    user = message.from_user.id
    text123 = 'FT'
    if user in config.USER:
        qwe = cursor.execute(
            f" SELECT lecture.FT FROM lecture WHERE lecture.fk_login_id = {user}")
        db.commit()
        button = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item = types.KeyboardButton('поставить НБ')
        item1 = types.KeyboardButton('В начало')
        button.add(item, item1)
        bot.send_message(message.chat.id, qwe, reply_markup=button)
    else:
        bot.send_message(message.chat.id, 'нет доступа')


@bot.message_handler(func=lambda message: message.text == 'Все предметы')
def lecture_ALL(message):
    db = sqlite3.connect('server.db')
    cursor = db.cursor()
    global user
    user = message.from_user.id
    if user in config.USER:
        qwe = cursor.execute(
            f" SELECT NERV, OFT, PED, AG, FH, FT FROM lecture WHERE lecture.fk_login_id = {user}")
        db.commit()
        bot.send_message(message.chat.id, qwe)
    else:
        bot.send_message(message.chat.id, 'нет доступа')


@bot.message_handler(func=lambda message: message.text == 'В начало')
def returns(message):
    global user
    user = message.from_user.id
    if user in config.USER:
            person1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Н,Г')
            item2 = types.KeyboardButton('ОФТ')
            item3 = types.KeyboardButton('ПЕД')
            item4 = types.KeyboardButton('АГ')
            item5 = types.KeyboardButton('ФХ')
            item6 = types.KeyboardButton('ФТ')
            item7 = types.KeyboardButton('Все предметы')
            person1.add(item1, item2, item3, item4, item5, item6, item7)
            bot.send_message(message.chat.id, '...', reply_markup=person1)
    else:
        bot.send_message(message.chat.id, 'нет доступа')


@bot.message_handler(func=lambda message: message.text == 'поставить НБ')
def NB(message):
    global user
    user = message.from_user.id
    if user in config.USER:
        bot.send_message(message.chat.id, 'Введите дату в формате dd,mm')

        @bot.message_handler(content_types=['text'])
        def lalala(message):
            db = sqlite3.connect('server.db')
            cursor = db.cursor()
            match text123:
                case 'NERV':
                    cursor.execute(f" INSERT INTO lecture(NERV , fk_login_id) VALUES ({message}, {user}) ")
                    db.commit()
                    bot.send_message(message.chat.id, 'НБ поставлено')
                case 'FT':
                    cursor.execute(f" INSERT INTO lecture(FT , fk_login_id) VALUES ({message}, {user}) ")
                    db.commit()
                    bot.send_message(message.chat.id, 'НБ поставлено')
                case 'FH':
                    cursor.execute(f" INSERT INTO lecture(FH , fk_login_id) VALUES ({message}, {user}) ")
                    db.commit()
                    bot.send_message(message.chat.id, 'НБ поставлено')
                case 'AG':
                    cursor.execute(f" INSERT INTO lecture(AG , fk_login_id) VALUES ({message}, {user}) ")
                    db.commit()
                    bot.send_message(message.chat.id, 'НБ поставлено')
                case 'OFT':
                    cursor.execute(f" INSERT INTO lecture(OFT , fk_login_id) VALUES ({message}, {user}) ")
                    db.commit()
                    bot.send_message(message.chat.id, 'НБ поставлено')
                case 'PED':
                    cursor.execute(f" INSERT INTO lecture(PED , fk_login_id) VALUES ({message}, {user}) ")
                    db.commit()
                    bot.send_message(message.chat.id, 'НБ поставлено')
    else:
        bot.send_message(message.chat.id, 'нет доступа')






# POLLING
bot.polling(none_stop=True)