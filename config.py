import os
from dotenv import load_dotenv

# Загрузка переменных из .env файла
load_dotenv()

# Чтение токена из переменной окружения
TOKEN = os.getenv("BOT_TOKEN")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

if not WEATHER_API_KEY:
    raise ValueError("Переменная окружения WEATHER_API_KEY не установлена!")

if not TOKEN:
    raise ValueError("Переменная окружения BOT_TOKEN не установлена!")