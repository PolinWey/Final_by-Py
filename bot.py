import telebot
import random
import json
import math
import os
import re
import sys
import datetime
import threading
import requests
from bs4 import BeautifulSoup
from les4 import pars

token = ''

bot = telebot.TeleBot(token)

number = 0

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = telebot.types.KeyboardButton('Отлично!')
    item2 = telebot.types.KeyboardButton('Хорошо')
    item3 = telebot.types.KeyboardButton('Норм')
    item4 = telebot.types.KeyboardButton('Да так...')
    item5 = telebot.types.KeyboardButton('Все плохо(')
    item6 = telebot.types.KeyboardButton('Давай дальше')

    markup.add(item1, item2, item3, item4, item5, item6)
    #bot.register_next_step_handler(message, mathsolving)
    bot.send_message(message.chat.id, 'Привет! Как дела? ', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == 'отлично!':
        bot.send_message(message.chat.id, 'Это прекрасно! Так держать!')
    elif message.text.lower() == 'хорошо':
        bot.send_message(message.chat.id, 'Не плохо, не плохо, так держать')
    elif message.text.lower() == 'норм':
        bot.send_message(message.chat.id, 'Хорошо, что не плохо)')
    elif message.text.lower() == 'да так...':
        bot.send_message(message.chat.id, 'Что-то ты приуныл(((')
    elif message.text.lower() == 'все плохо(':
        bot.send_message(message.chat.id, 'Все наладится!')
    elif message.text.lower() == 'давай дальше':
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = telebot.types.KeyboardButton('Рандомное число')
        item2 = telebot.types.KeyboardButton('Камни и минералы')
        item3 = telebot.types.KeyboardButton('Вернемся назад')
        markup.add(item1, item2, item3)
        bot.send_message(message.chat.id, 'Выбери из предложенного', reply_markup=markup)
        bot.register_next_step_handler(message, welcome)
        if message.text.lower() == 'рандомное число':
            bot.send_message(message.chat.id, str(random.randint(1, 1000)))

@bot.message_handler(commands=['start'])
def seconds(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = telebot.types.KeyboardButton('Рандомное число')
    item2 = telebot.types.KeyboardButton('Камни и минералы')
    item3 = telebot.types.KeyboardButton('Вернемся назад')

    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, 'Выбери из предложенного', reply_markup=markup)
    bot.register_next_step_handler(message, seconds)

@bot.message_handler(content_types=['text'])
def answer(message):
    if  message.text.lower() == 'рандомное число':
        bot.send_message(message.chat.id, str(random.randint(1, 1000)))
    elif message.text.lower() == 'камни и минералы':
        bot.send_message(message.chat.id, 'Все наладится!')






bot.polling(none_stop=True)