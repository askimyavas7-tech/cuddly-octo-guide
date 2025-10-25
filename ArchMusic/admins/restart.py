import os, sys
from pyrogram import Client, filters
from config import OWNER_ID

@Client.on_message(filters.command("restart") & filters.user(lambda _, __, m: OWNER_ID and m.from_user and m.from_user.id == OWNER_ID))
async def restart_cmd(client, message):
    await message.reply_text("♻️ Yeniden başlatılıyor...")
    os.execv(sys.executable, [sys.executable, "-m", "ArchMusic.core.bot"])
