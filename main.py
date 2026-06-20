# main.py — BreadFastBot: регистрация бота и первое сообщение
import os

from dotenv import load_dotenv
from telegram import Bot

load_dotenv()  # читает .env из корня репозитория

# Секреты — из .env (не хардкодим: репозиторий уходит в Git):
#   BOT_TOKEN  — токен от @BotFather
#   MY_CHAT_ID — твой Telegram ID
bot = Bot(token=os.environ["BOT_TOKEN"])
chat_id = os.environ["MY_CHAT_ID"]

# Текст сообщения
text = "Вам телеграмма!"

# Отправка. Аргументы строго ПОЗИЦИОННО: send_message(chat_id, text) —
# именно так этого ждёт автотест: assert_called_once_with(chat_id, text).
bot.send_message(chat_id, text)
