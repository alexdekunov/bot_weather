import os
from dotenv import load_dotenv


# Загрузка переменных окружения из файла .env
load_dotenv()

# Использование переменных окружения в приложении
api_t = os.getenv('API_TELEGRAM')
api_w = os.getenv('API_WEATHER')

