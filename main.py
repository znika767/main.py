import telebot

bot = telebot.TeleBot('7193341679:AAHXbhHqpGxnq5UOS6H_tsUld-WcQfFSb9M')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '<b>Hello!</b>', parse_mode='html')



bot.polling(non_stop=True)