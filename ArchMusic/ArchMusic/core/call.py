import logging
from pyrogram import Client
from py_tgcalls import PyTgCalls
from py_tgcalls.types import AudioPiped
from py_tgcalls.exceptions import GroupCallNotFound

log = logging.getLogger("ArchMusic")

class CallManager:
    def __init__(self, client: Client):
        self.client = client
        self.call = PyTgCalls(client)

    async def start(self):
        try:
            await self.call.start()
            log.info("✅ Ses sistemi (Py‑TgCalls) başlatıldı.")
        except Exception as e:
            log.error(f"❌ Ses sistemi başlatılamadı: {e}")

    async def play(self, chat_id: int, audio_file: str):
        try:
            await self.call.join_group_call(chat_id, AudioPiped(audio_file))
            log.info(f"🎵 Çalma başladı: {audio_file}")
        except GroupCallNotFound:
            log.warning("⚠️ Grup çağrısı yok. Önce sesli sohbeti başlatın.")
        except Exception as e:
            log.error(f"❌ Ses çalma hatası: {e}")

    async def stop(self):
        try:
            await self.call.stop()
            log.info("🛑 Ses sistemi durduruldu.")
        except Exception:
            pass
