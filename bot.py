import telebot
import config
from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
  if message.from_user.id in config.USER: 
    def lox(message):
      keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
      item1 = types.KeyboardButton('отметить НБ')
      item2 = types.KeyboardButton('убрать НБ')
      keyboard.add(item1, item2)
      bot.send_message(message.chat.id, text = 'что вам надо?', reply_markup=keyboard)
    lox(message)

    @bot.message_handler(content_types=['text'])
    def lalala(message):
      if message.text == 'отметить НБ':
        person1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Н, Г')
        item2 = types.KeyboardButton('ОФТ')
        item3 = types.KeyboardButton('Пед')
        item4 = types.KeyboardButton('АГ')
        item5 = types.KeyboardButton('ФХ')
        item6 = types.KeyboardButton('ФТ')
        item7 = types.KeyboardButton('В начало')
        person1.add(item1, item2, item3, item4, item5, item6, item7)
        bot.send_message(message.chat.id, '...', reply_markup=person1)
        

        if(message.text == 'ОФТ'):
          bot.send_message(message.chat.id, 'ты лох', reply_markup=person1)



      elif message.text == 'убрать НБ':
        person2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Н, Г')
        item2 = types.KeyboardButton('ОФТ')
        item3 = types.KeyboardButton('Пед')
        item4 = types.KeyboardButton('АГ')
        item5 = types.KeyboardButton('ФХ')
        item6 = types.KeyboardButton('ФТ')
        person2.add(item1, item2, item3, item4, item5, item6)
        bot.send_message(message.chat.id, '...', reply_markup=person2)

    lalala(message)  

  else:
      bot.send_message(message.chat.id, 'нет доступа')
  bot.polling(none_stop=True)