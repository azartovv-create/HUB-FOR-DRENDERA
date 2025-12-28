import telebot
import os
from telebot import types

TOKEN = os.getenv("8341434584:AAGG_J_z-Arh0PTE5vIEFRpz_eadg4uxCdI")
bot = telebot.TeleBot(TOKEN)

CHANNELS = ["@USANEWRAP", "@USAGANGG"]  # замени на свои каналы
ACCESS_LINK = "https://t.me/+UBna5Mr2-HQxY2Ri"  # ссылка на приватный канал

@bot.message_handler(commands=["start"])
def start(message):
    chat_id = message.chat.id
    markup = types.InlineKeyboardMarkup()
    for channel in CHANNELS:
        markup.add(types.InlineKeyboardButton(f"Подписаться на {channel}", url=f"https://t.me/{channel[1:]}"))
    markup.add(types.InlineKeyboardButton("Далее", callback_data="check_subs"))

    bot.send_message(
        chat_id,
        "Привет! 👋\nЧтобы получить доступ, подпишись на наши каналы и нажми 'Далее'.",
        reply_markup=markup
    )

@bot.callback_query_handler(func=lambda call: call.data == "check_subs")
def check_subs(call):
    chat_id = call.message.chat.id
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Перейти в приват", url=ACCESS_LINK))

    bot.send_message(
        chat_id,
        "Отлично! В привате будут выходить ежедневные сливы твоих любимых артистов.\n"
        "Включите уведомления в наших каналах, чтобы ничего не пропустить!",
        reply_markup=markup
    )

bot.infinity_polling()