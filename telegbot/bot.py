# -*- coding: utf-8 -*-
import random

import telebot

TOKEN = '311637383:AAFS1-pZNsec0ZUIZjqyq_n8A2KiHOkR5nU'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hey')


first_answers = ['Привет-привет, как жизнь?','Какие люди, как дела?','Давно не виделись, как ты?','Приветики!']

@bot.message_handler(rexept="Привет")
def echo1(message):
    if message.text == 'привет' or 'Привет':
        bot.send_message(message.chat.id, random.choice(first_answers))

@bot.message_handler(rexept="Что ты умеешь?")
def echo2(message):
    if message.text == 'Что ты умеешь?':#'что ты умеешь?','Что ты можешь?','что ты можешь?','кто ты?','Кто ты?':
        bot.send_message(message.chat.id, '''Я - первый бот Создателя, сделан во имя домашней практики, вот краткий 
перечень того что я умею:
Загадать тебе загадки
Покидать мемасы
Подсказать время
''')
как_дела = ['Норм','Отлично','Всё путём']
@bot.message_handler(content_types=["text"])
def echo3(message):
    if message.text == 'Как дела?':
        bot.reply_to(message, random.choice(как_дела))
        bot.send_message(message.chat.id, "Сам как?")



if __name__ == '__main__':
    bot.polling()