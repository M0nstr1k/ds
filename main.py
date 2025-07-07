import telebot
from telebot import types

TOKEN = "8148136479:AAG-Hz9XWqDN-H5hYMENE_NdfUSly1Rg35w"

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start", "help"])
@bot.message_handler(func=lambda m: True)
def send_message(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("ЖМИ", callback_data="press"))
    bot.send_message(message.chat.id, "ХОЧЕШЬ СИСЬКИ? НАЖИМАЙ КНОПКУ НИЖЕ", reply_markup=markup)


@bot.callback_query_handler(func=lambda c: c.data == "press")
def button_pressed(call):
    bot.answer_callback_query(call.id, "Кнопка нажата!")


if __name__ == "__main__":
    bot.infinity_polling()
