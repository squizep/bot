import telebot
import config
from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
  markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
  item1 = types.KeyboardButton('отметить НБ')
  item2 = types.KeyboardButton('убрать НБ')
  markup.add(item1, item2)
  bot.send_message(message.chat.id, 'что вам надо?', reply_markup=markup)
@bot.message_handler(content_types=['text'])
def lalala(message):
  if message.chat.type == 'private':
    if message.text == 'привет':
      bot.send_message(message.chat.id, 'привет')

bot.polling(none_stop=True)