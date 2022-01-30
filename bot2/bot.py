import telebot
from telebot import types

bot = telebot.TeleBot("5055862569:AAFpqAhbN4O0WWHBW2osA2jtIxt3GFTUm8o")

@bot.message_handler(commands=["start"])
def start(message):
    channel_link = "https://t.me/qwerasdftygewe"
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard = types.KeyboardButton("Подтвердить")
    markup.add(keyboard)
    chat_id = message.chat.id
    user = message.chat.first_name
    bot.send_message(chat_id, f"qq {user} подпишись чтобы пользоваться мною\n"
							       f"{channel_link}", reply_markup=markup)


		
@bot.message_handler(content_types=["text"])
def bot_message(message):
    user = message.chat.first_name
    if message.chat.type == 'private':
        if message.text == 'Подтвердить':
                status = ['creator', 'administrator', 'member']
                for stat in status:
                    if stat == bot.get_chat_member(chat_id="@qwerasdftygewe", user_id=message.from_user.id).status:
                        bot.send_message(message.chat.id, f" {user} Спасибо что подписались на канл!")
                    break

                else:
                    bot.send_message(message.chat.id, f" {user} Кажется вы не подписались !")

bot.polling(none_stop=True)