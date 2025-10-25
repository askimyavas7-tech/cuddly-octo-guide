import subprocess
from .logger import setup_logging

log = setup_logging()

def fetch_updates(upstream: str):
    try:
        subprocess.run(["git", "fetch", upstream], check=True)
        log.info("Git upstream fetched successfully.")
    except FileNotFoundError:
        log.warning("Git fetch skipped: 'git' binary not found on this dyno.")
    except Exception as e:
        log.warning(f"Git fetch skipped: {e}")
