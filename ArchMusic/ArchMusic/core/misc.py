from .logger import setup_logging

log = setup_logging()

def init_database():
    log.info("Database Initialized.")

def load_sudoers():
    log.info("Sudoers Loaded.")
