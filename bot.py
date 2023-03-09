import telebot
import config
from telebot import types



bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    if message.from_user.id in config.USER: 
        person1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Н,Г')
        item2 = types.KeyboardButton('ОФТ')
        item3 = types.KeyboardButton('Пед')
        item4 = types.KeyboardButton('АГ')
        item5 = types.KeyboardButton('ФХ')
        item6 = types.KeyboardButton('ФТ')
        person1.add(item1, item2, item3, item4, item5, item6)
        bot.send_message(message.chat.id, '...', reply_markup=person1)

    else:
        bot.send_message(message.chat.id, 'нет доступа')

@bot.message_handler(content_types=['text'])
def lalala(message):
    match message.text:
        case 'Н,Г':
            #должны выводиться все даты с БД
            bot.send_message(message.chat.id, 'ты лох')
        case 'ОФТ':
            bot.send_message(message.chat.id, 'ты лох')
        case 'Пед':
            bot.send_message(message.chat.id, 'ты лох')
        case 'АГ':
            bot.send_message(message.chat.id, 'ты лох')
        case 'ФХ':
            bot.send_message(message.chat.id, 'ты лох')
        case 'ФТ':
            bot.send_message(message.chat.id, 'ты лох')
        case _:
            pass
bot.polling(none_stop=True)