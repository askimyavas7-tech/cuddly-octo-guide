import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID", "0"))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

LOG_GROUP_ID = int(os.getenv("LOG_GROUP_ID", "0"))
OWNER_ID = int(os.getenv("OWNER_ID", "0")) if os.getenv("OWNER_ID") else None

MONGO_DB_URI = os.getenv("MONGO_DB_URI", "")

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID", "")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET", "")

UPSTREAM_REPO = os.getenv("UPSTREAM_REPO", "")

MUSIC_BOT_NAME = os.getenv("MUSIC_BOT_NAME", "Prenses Müzik Pro")
