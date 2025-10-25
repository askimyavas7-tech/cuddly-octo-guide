# Prenses Müzik Pro

Heroku-uyumlu, Pyrogram + Py‑TgCalls tabanlı Telegram müzik botu.

## Hızlı Kurulum (Heroku)
1) **Buildpacks**
   - `https://github.com/jonathanong/heroku-buildpack-ffmpeg-latest`
   - `heroku/python`
2) **Config Vars**
   - `API_ID`, `API_HASH`, `BOT_TOKEN`
   - `LOG_GROUP_ID` (ör. `-100xxxxxxxxxx`)
   - `MONGO_DB_URI` (opsiyonel; yoksa bot logs’a uyarı yazar)
   - `SPOTIFY_CLIENT_ID` ve `SPOTIFY_CLIENT_SECRET` (opsiyonel)
   - `OWNER_ID` (sahip telegram id)
3) **Dyno**
   - Resources > `worker` dyno’yu aç.
