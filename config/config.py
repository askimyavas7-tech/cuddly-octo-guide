import os
from dotenv import load_dotenv
load_dotenv()  # Heroku'da şart değil ama lokal için iyi

API_ID = int(os.getenv("API_ID", "0"))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

LOG_GROUP_ID = int(os.getenv("LOG_GROUP_ID", "0"))
OWNER_ID = int(os.getenv("OWNER_ID", "0"))

MONGO_DB_URI = os.getenv("MONGO_DB_URI", "")
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID", "")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET", "")

ASSISTANT_USERNAME = os.getenv("ASSISTANT_USERNAME", "")  # @Pars_asistan gibi
UPSTREAM_REPO = os.getenv("UPSTREAM_REPO", "")

# Basit kara liste ve admin list placeholder'ları (app.json uyumu için)
BANNED_USERS = set()
adminlist = {}
