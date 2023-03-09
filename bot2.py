if message.text == 'отметить НБ':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('отметить НБ')
        item2 = types.KeyboardButton('убрать НБ')
        keyboard.add(item1, item2)
        bot.send_message(message.chat.id, text = 'что вам надо?', reply_markup=keyboard)

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
