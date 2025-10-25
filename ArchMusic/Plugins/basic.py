from pyrogram import Client, filters
from config import MUSIC_BOT_NAME

@Client.on_message(filters.command(["start", "help"]))
async def start_help(client, message):
    txt = (
        f"✨ **{MUSIC_BOT_NAME}**\n\n"
        "Komutlar:\n"
        "- /ping: Botun gecikmesini gösterir.\n"
        "- /play <link/şarkı adı>: (örnek, ses sistemi hazır)\n"
    )
    await message.reply_text(txt)

@Client.on_message(filters.command("ping"))
async def ping(client, message):
    await message.reply_text("🏓 Pong!")
