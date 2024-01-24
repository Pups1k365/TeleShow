import random
import sqlite3
from telebot import TeleBot, types
from telebot.types import InputMediaPhoto
import requests
from datetime import datetime

bot = TeleBot("6698589877:AAFXaBwoeSeUPwYufRJYRqXL7jjTcDRkK5A")

conn = sqlite3.connect('data.db')
c = conn.cursor()

# Create the Admin table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS Admin (
    cid INTEGER,
    lvl INTEGER
)''')

def is_admin(cid):
    conn = sqlite3.connect('C:/Users/Admin/Desktop/Проекты/!!!/BrawlHn/data.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Admin WHERE cid=? AND lvl > 2", (cid,))
    data = cursor.fetchone()

    if data is not None:
        return True

    cursor.execute("SELECT * FROM vip WHERE cid=? AND lvl >= 1", (cid,))
    data_vip = cursor.fetchone()

    if data_vip is not None:
        return True

    return False

def is_admin_level(cid, level):
    conn = sqlite3.connect('C:/Users/Admin/Desktop/Проекты/!!!/BrawlHn/data.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Admin WHERE cid=? AND lvl >= ?", (cid, level))
    data = cursor.fetchone()

    if data is not None:
        return True

    return False

image_data = {
    "пайпер": [
        [
            InputMediaPhoto(media="https://wimg.rule34.xxx//images/7703/ae296a9a27068047051ba1ac3f8775a2.jpeg?8794480", caption="📌 | #пайпер", has_spoiler=True),
            InputMediaPhoto(media="https://wimg.rule34.xxx//images/7703/278986bb0136aa3959eea9a0a8393d06.jpeg?8794501", has_spoiler=True),
            InputMediaPhoto(media="https://wimg.rule34.xxx//images/7703/74cbd1fd26ded12b505e20c16a6a2db6.jpeg?8794527", has_spoiler=True)
        ],
        [
            InputMediaPhoto(media="https://rule34.xxx//samples/5380/sample_9b882ef0bf0bb67e09ea13a87253a0d6.jpg?6128340", caption="📌 | #пайпер", has_spoiler=True),
            InputMediaPhoto(media="https://rule34.xxx//samples/5380/sample_2c65a34076a23e6c1b3b83adc7d36840.jpg?6128342", has_spoiler=True),
        ],
        [
            InputMediaPhoto(media="https://uvdmain.000webhostapp.com/image/piper_n_n1.jpg", caption="📌 | #пайпер #Ai", has_spoiler=True),
            InputMediaPhoto(media="https://uvdmain.000webhostapp.com/image/piper_n1.jpg", has_spoiler=True),
        ],
        [
            InputMediaPhoto(media="https://uvdmain.000webhostapp.com/image/piper_n2.jpg", caption="📌 | #пайпер", has_spoiler=True),
            InputMediaPhoto(media="https://uvdmain.000webhostapp.com/image/piper_n_n2.jpg", has_spoiler=True),
        ],
    ],
    "new": [
        [
            InputMediaPhoto(media="https://uvdmain.000webhostapp.com/image/piper_n_n3.jpg", caption="📌 | #пайпер #AI\n⚠️ | <i>Больше изображении/видео:</i> @Brawlhnbot", has_spoiler=True ,parse_mode="HTML"),
            InputMediaPhoto(media="https://uvdmain.000webhostapp.com/image/piper_n_3.jpg", has_spoiler=True),

        ]
    ],
    "чарли": [
        [
			InputMediaPhoto(media="https://wimg.rule34.xxx//images/2304/c3037f2e6bc9cc9660606e02d99856e4.png?9325521", caption="📌 | #чарли #ai\n⚠️ | <b>Naked AI by @pups1k666</b>", has_spoiler=True ,parse_mode="HTML"),
			InputMediaPhoto(media="https://uvdmain.000webhostapp.com/photo_2024-01-21_08-55-51.jpg", has_spoiler=True),
        ]
    ],
    "беа": [
		[
			InputMediaPhoto(media="https://uvdmain.000webhostapp.com/beano228.jpg",caption="📌 | #беа #ai\n⚠️ | <b>Naked AI by @pups1k666</b>", has_spoiler=True ,parse_mode="HTML"),
			InputMediaPhoto(media="https://uvdmain.000webhostapp.com/beayes228.jpg", has_spoiler=True),
        ]
    ]
}

@bot.message_handler(commands=['hn'])
def send_images(message):
    if not is_admin(message.from_user.id):
        bot.reply_to(message, "🔱 | <b>Эта команда доступна для пользователей VIP.</b>", parse_mode="HTML")
       
        return

    if '-' in str(message.chat.id):
        bot.reply_to(message, "нельзя")
        return

    if message.text == '/hn':
        bot.reply_to(message, "🔱 | <b>VIP КОМАНДА</b> | 🔱\n🔰 | <i>Эта команда предоставляет случайные хентай изображения/видео по указанному персонажу/тематике.</i>\n\n⚠️ | <b>Укажите персонажа\тематику.</b>\n♻️ | <b>Например:</b> <code>/hn пайпер</code>", parse_mode="HTML")
        return

    args = message.text.split(' ')
    if len(args) < 2:
        bot.reply_to(message, "🔱 | <b>VIP КОМАНДА</b> | 🔱\n🔰 | <i>Эта команда предоставляет случайные хентай изображения/видео по указанному персонажу/тематике.</i>\n\n⚠️ | <b>Укажите персонажа\тематику.</b>\n♻️ | <b>Например:</b> <code>/hn пайпер</code>", parse_mode="HTML")
        return

    keyword = args[1].strip()

    if keyword in image_data:
        Ouid = message.from_user.username
        uid = message.from_user.id
        cid = message.chat.id
        media_options = image_data[keyword]
        selected_media = random.choice(media_options)
        bot.send_media_group(message.chat.id, selected_media, reply_to_message_id=message.message_id)
        bot.send_message(-1002016297566, f"🫂 | <b>Команда: <code>{args[0]} {args[1]}</code></b>\n♟ | [Telegram: @{Ouid}]\n💬 | [CHAT_USER: {uid}] - [CHAT_ID: {cid}]", parse_mode="HTML")
    else:
        bot.reply_to(message, "⚠️ |<b>Персонаж/тематика не найдена.</b>\n♻️ | <b>Например:</b> <code>/hn шелли</code>", parse_mode="HTML")


@bot.message_handler(commands=['givevip'])
def give_vip(message):
    if not is_admin(message.from_user.id) or not is_admin_level(message.from_user.id, 5):
        bot.reply_to(message, "🅰️ | <b>Вы не имеете права на использование этой команды.</b>")
        return
    args = message.text.split(' ')
    if len(args) != 3:
        bot.reply_to(message, "Используйте команду в формате /givevip [cid] [lvl]")
        return
    cid = args[1]
    lvl = args[2]
    conn = sqlite3.connect('C:/Users/Admin/Desktop/Проекты/!!!/BrawlHn/data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM vip WHERE cid=?", (cid,))
    existing_record = cursor.fetchone()
    if existing_record:
        if lvl == '0':
            cursor.execute("DELETE FROM vip WHERE cid=?", (cid,))
            conn.commit()
            conn.close()
            bot.reply_to(message, f"Пользователь с id {cid} удален из VIP.")
        else:
            cursor.execute("UPDATE vip SET lvl=? WHERE cid=?", (lvl, cid))
            conn.commit()
            conn.close()
            bot.reply_to(message, f"Уровень VIP пользователя с id {cid} обновлен на {lvl}.")
    else:
        cursor.execute("INSERT INTO vip (cid, lvl) VALUES (?, ?)", (cid, lvl))
        conn.commit()
        conn.close()
        bot.reply_to(message, f"Пользователь с id {cid} назначен VIP уровня {lvl}.")


@bot.message_handler(commands=['viplist'])
def vip_list(message):
    if not is_admin(message.from_user.id):
        bot.reply_to(message, "Эта команда доступна только администраторам уровня 2 и выше.")
        return
    conn = sqlite3.connect('C:/Users/Admin/Desktop/Проекты/!!!/BrawlHn/data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT cid, lvl FROM vip")
    vip_users = cursor.fetchall()
    conn.close()
    if vip_users:
        response = "🔱 | <b>Список пользователей с VIP-статусом:</b>\n"
        for user in vip_users:
            user_info = bot.get_chat_member(user[0], user[0])
            user_name = user_info.user.first_name
            response += f"<b>{user_name}</b>(<code>{user[0]}</code>), Уровень VIP: {user[1]}\n"
        bot.reply_to(message, response, parse_mode="HTML")
    else:
        bot.reply_to(message, "На данный момент нет пользователей с VIP-статусом.")

type_translation = {
    "пайпер": "piper",
    "фэнг": "fang",
	"эдгар": "edgar",
	"колетт": "colette",
	"шелли": "shelly",
	"кольт": "colt",
	"эмз": "emz",
}

@bot.message_handler(commands=['stats'])
def send_stats_image(message):
    if len(message.text.split()) == 1:
        bot.reply_to(message, "⚠️ | <b>Напишите свой ID</b>\n♻️ | Например: <code>/stats Y0CQY90VQ колетт</code>", parse_mode='HTML')
    else:
        values = message.text.split(' ')
        player_id = values[1]
        image_type = "best"  
        if len(values) > 2:
            requested_type = values[2].lower()
            image_type = type_translation.get(requested_type, requested_type)
        try:
            image_url = f"https://www.brawltime.ninja/api/render/profile/{player_id}/{image_type}.png?background=cartoon_lobby.jpg"
            response = requests.get(image_url)
            if response.status_code == 200:
                photo = open('temp_image.png', 'wb')
                photo.write(response.content)
                photo.close()
                with open('temp_image.png', 'rb') as photo:
                    bot.send_photo(message.chat.id, photo, reply_to_message_id=message.message_id)
            else:
                bot.reply_to(message, f"⚠️ | Произошла ошибка: {response.status_code}. Пожалуйста, попробуйте еще раз.")
        except Exception as e:
            bot.reply_to(message, f"⚠️ | Произошла ошибка: {e}. Пожалуйста, попробуйте еще раз.")
		
@bot.message_handler(commands=['cid'])
def cid_handler(message):
    chat_id = message.chat.id
    bot.reply_to(message, f"{chat_id}")
	
start_time = datetime.now()

@bot.message_handler(commands=['infobot'])
def infobot_handler(message):
    current_time = datetime.now()
    uptime = current_time - start_time
    hours, remainder = divmod(uptime.seconds, 3600)
    minutes, _ = divmod(remainder, 60)
    bot.reply_to(message, f"Время работы бота: {hours} ч. {minutes} м.")
bot.polling()
