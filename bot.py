import telebot
from config import bot_token

bot = telebot.TeleBot(bot_token)

@bot.message_handler(content_types=['text'])
def echo(message):
    bot.send_message(message.chat.id, message.text)


bot.polling(none_stop=True)