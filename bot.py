import telebot
import config

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['trigger'])
def trigger(message):
    bot.send_message(message.chat.id, "Всем чатом осуждаем Николая и Лёву за то что они не нашли работу")


@bot.message_handler(content_types=['text'])
def bottalk(message):
    bot.send_message(message.chat.id, message.text)

#RUN

bot.polling(none_stop=True)
