import telebot
import os
from datetime import datetime

TOKEN = '5942635111:AAHpSN0GqJ0CR8ERVSFf8H-tS3QYYRwZTok'

bot = telebot.TeleBot(TOKEN)

start_time = datetime.now()


@bot.message_handler(commands=['infobot'])
def infobot_handler(message):
  current_time = datetime.now()
  uptime = current_time - start_time
  hours, remainder = divmod(uptime.seconds, 3600)
  minutes, _ = divmod(remainder, 60)

  ping = (datetime.now() - current_time).microseconds / 1000

  if os.path.exists('data.db'):
    db_status = "успешно"
  else:
    db_status = "потеря соединения"

  response = (
      f"ℹ️| <b>Время работы бота</b>: {hours} ч. {minutes} м.\n📶 | <b>Пинг:</b> {ping} мс.\n🈁 | <b>База данных</b>: {db_status}"
  )
  bot.reply_to(message, response, parse_mode='HTML')

bot.polling()
