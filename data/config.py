import os

from dotenv import load_dotenv

load_dotenv()

SERVER_PORT = int(os.environ.get('PORT', 80))
ADMIN_CHAT_ID = int(os.getenv("ADMIN_CHAT_ID"))
BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
CAT_API_KEY = str(os.getenv("CAT_API_KEY"))

WH_SERVER_URL = str(os.getenv("WH_SERVER_URL")) if "WH_SERVER_URL" in list(
    os.environ.keys()) else None

cat_api_url = 'https://api.thecatapi.com/v1/images/search'

DB_CONF = {
    'host': str(os.getenv("DB_HOST")),
    'user': str(os.getenv("DB_USER")),
    'database': str(os.getenv("DB_DATABASE")),
    'password': str(os.getenv("DB_PASSWORD")),
    'port': str(os.getenv("DB_PORT"))
}

GAME_INIT_SETTINGS = {
    "acts": {
        "fascist": 11,
        "liberal": 6
    },
    "max_players": 10,
    "min_players": 5,
}
