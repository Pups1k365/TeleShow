import telebot

TOKEN = '5942635111:AAHpSN0GqJ0CR8ERVSFf8H-tS3QYYRwZTok'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['привет'])
def send_hello(message):
    bot.reply_to(message, "пока")

bot.polling()
