import logging
from pyrogram import Client
from py_tgcalls import PyTgCalls

log = logging.getLogger("ArchMusic")

class CallManager:
    def __init__(self, client: Client):
        self.client = client
        self.call = PyTgCalls(client)

    async def start(self):
        try:
            await self.call.start()
            log.info("🎧 PyTgCalls ses sistemi açıldı.")
        except Exception as e:
            log.warning(f"PyTgCalls başlatılamadı: {e}")

    async def stop(self):
        try:
            await self.call.stop()
            log.info("🛑 PyTgCalls durdu.")
        except Exception:
            pass
