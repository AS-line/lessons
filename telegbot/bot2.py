import telebot

TOKEN = '311637383:AAFS1-pZNsec0ZUIZjqyq_n8A2KiHOkR5nU'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['my_kb'])
def start(message):
    bot.send_message(message.chat.id, 'Отправь название фильма')

@bot.message_handler(commands=['getsite'])
def spoilering(message):
    line_kb = telebot.types.InlineKeyboardMarkup()
    url_btn = telebot.types.InlineKeyboardButton('Лучшие мемасы перишков!', url = 'https://github.com/')
    url_btn2 = telebot.types.InlineKeyboardButton('-->Жми сюды<--', url = 'https://t.me/perimemes/')
    line_kb.add(url_btn)
    line_kb.add(url_btn2)
    bot.send_message(message.chat.id, 'Жми',reply_markup = line_kb)  




if __name__ == '__main__':
    bot.polling()