import os
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv("TGBotToken")
WEATHER_API_KEY = os.getenv("OpenWeatherMapAPIKey")

if not WEATHER_API_KEY:
    raise ValueError("Переменная окружения WEATHER_API_KEY не установлена!")

if not TOKEN:
    raise ValueError("Переменная окружения BOT_TOKEN не установлена!")