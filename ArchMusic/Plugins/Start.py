from pyrogram import filters
from pyrogram.types import Message
import os

@filters.client.on_message(filters.command(["start", "help"]) & filters.private)
async def start_handler(client, message: Message):
    owner = os.getenv("OWNER_ID", "-")
    await message.reply_text(
        "🎵 **Prenses Müzik Pro**\n\n"
        "Bot çalışıyor. Grup içinde komutları kullanabilirsin.\n"
        f"👑 Owner: `{owner}`"
    )
