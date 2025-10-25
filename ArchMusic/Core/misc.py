import logging
import os

log = logging.getLogger("ArchMusic")

# Basit bellek taklitleri
SUDOERS = set()

def init_database():
    # Burada gerçek DB bağlantısı kurabilirsin (opsiyonel)
    log.info("Database Initialized.")

def load_sudoers():
    owner = os.getenv("OWNER_ID")
    if owner:
        try:
            SUDOERS.add(int(owner))
        except:
            pass
    log.info("Sudoers Loaded.")
