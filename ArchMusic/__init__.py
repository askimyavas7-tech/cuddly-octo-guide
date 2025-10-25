# ArchMusic package initializer

from .core.logger import setup_logging
LOGGER = setup_logging("INFO")

# Eski pluginlerle uyumluluk için global 'app'
# bot.py içinde gerçek Client örneği buraya atanır.
app = None

LOGGER.info("✅ ArchMusic paket yüklemesi tamamlandı.")
