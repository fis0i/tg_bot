import telebot
from telebot import types
from cfg import api

bot = telebot.TeleBot(api)


@bot.message_handler(commands=['start', 'help'])
def start(message):
    if message.text == '/start':
        mess = f'Привет, <b>{message.from_user.first_name} ! \n' \
               f'Выбери в меню, что хотел бы сделать. \n' \
               f'Если не нашел, что искал - пиши /help</b>'
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        teacher = types.KeyboardButton('Расписание преподавателей.')
        rasp = types.KeyboardButton('Расписание занятий 3збАСУп.')
        markup.add(rasp, teacher)
        bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)
        print(f'{message.from_user.first_name} {message.from_user.last_name}')
    elif message.text == '/help':
        bot.send_message(message.chat.id, 'Пошел нахуй')


@bot.message_handler(content_types='text')
def top(message):
    if message.text == 'Расписание преподавателей.':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        makarenko = types.KeyboardButton('Макаренко Л.Ф.')
        salniy = types.KeyboardButton('Сальный А.Г.')
        mezen = types.KeyboardButton('Мезенцев К.Н.')
        plet = types.KeyboardButton('Плетнева Л.А.')
        mat = types.KeyboardButton('Матюхина Е.Н')
        vasil = types.KeyboardButton('Васильева Ю.И.')
        afanasiev = types.KeyboardButton('Афанасьев В.В.')
        back = types.KeyboardButton('Назад')
        markup.add(makarenko, salniy, mezen, plet, mat, vasil, afanasiev, back)
        bot.send_message(message.chat.id, 'Выберите преподавателя', parse_mode='html', reply_markup=markup)
    elif message.text == 'Расписание занятий 3збАСУп.':
        photo = open('static/rasp1.jpg', 'rb')
        photo2 = open('static/rasp2.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_photo(message.chat.id, photo2)
    if message.text == 'Макаренко Л.Ф.':
        photo = open('static/Makarenko.png', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == 'Сальный А.Г.':
        photo = open('static/Salniy.png', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == 'Мезенцев К.Н.':
        photo = open('static/Mezen1.png', 'rb')
        photo2 = open('static/Mezen2.png', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_photo(message.chat.id, photo2)
    elif message.text == 'Плетнева Л.А.':
        photo = open('static/Pletneva.png', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == 'Матюхина Е.Н':
        photo = open('static/Matykh.png', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == 'Васильева Ю.И.':
        photo = open('static/Vasilyeva.png', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == 'Афанасьев В.В.':
        photo = open('static/Afanasiev.png', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == 'Назад':
        mess = f'<b>Выбери в меню, что хотел бы сделать. \n' \
               f'Если не нашел, что искал - пиши /help</b>'
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        teacher = types.KeyboardButton('Расписание преподавателей.')
        rasp = types.KeyboardButton('Расписание занятий 3збАСУп.')
        markup.add(rasp, teacher)
        bot.send_message(message.chat.id, mess, parse_mode='html',
                         reply_markup=markup)
        print(f'{message.from_user.first_name} {message.from_user.last_name}')


bot.polling(none_stop=True)


# @bot.message_handler()
# def get_user_text(message):
#     if message.text == 'Hello':
#         bot.send_message(message.chat.id, 'Привет', parse_mode='html')
#     elif message.text == 'id':
#         bot.send_message(message.chat.id, f'Твой ID: {message.from_user.id}', parse_mode='html')
#     elif message.text == 'photo':
#         photo = open('bird.jpg', 'rb')
#         bot.send_photo(message.chat.id, photo)
#         print(f'{message.from_user.first_name} {message.from_user.last_name}')
#     else:
#         bot.send_message(message.chat.id, 'Я тебя не понимаю', parse_mode='html')