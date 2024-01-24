import telebot
import requests

bot = telebot.TeleBot('6698589877:AAFXaBwoeSeUPwYufRJYRqXL7jjTcDRkK5A')

@bot.message_handler(commands=['info'])
def check_website_availability(message):
    if len(message.text.split()) == 1:
        bot.reply_to(message, "⚠️ | Напишите ссылку на сайт для проверки доступности")
    else:
        website_url = message.text.split()[1]
        try:
            response = requests.get(website_url)
            if response.status_code == 200:
                bot.reply_to(message, "✅ | Сайт доступен")
            else:
                bot.reply_to(message, f"⚠️ | Сайт недоступен. Код состояния: {response.status_code}")
        except Exception as e:
            bot.reply_to(message, f"⚠️ | Произошла ошибка при проверке сайта: {e}")

bot.polling()
