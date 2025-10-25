import shutil
import subprocess
import logging

log = logging.getLogger("ArchMusic")

def fetch_updates(repo_url: str):
    """Opsiyonel: Git yoksa sessizce geç."""
    if not shutil.which("git"):
        log.warning("Git fetch atlandı: sistemde 'git' yok.")
        return
    try:
        subprocess.run(["git", "remote", "set-url", "origin", repo_url], check=True)
        subprocess.run(["git", "fetch", "origin"], check=True)
        log.info("Upstream kontrol edildi.")
    except Exception as e:
        log.warning(f"Git fetch atlandı: {e}")
