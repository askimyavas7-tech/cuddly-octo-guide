import logging
import sys

def setup_logging(level: str = "INFO"):
    logger = logging.getLogger()
    if logger.handlers:
        return logging.getLogger("ArchMusic")
    logger.setLevel(getattr(logging, level.upper(), logging.INFO))
    h = logging.StreamHandler(sys.stdout)
    fmt = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s", "%H:%M:%S")
    h.setFormatter(fmt)
    logger.addHandler(h)
    return logging.getLogger("ArchMusic")
