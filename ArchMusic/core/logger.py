import logging
import sys

def setup_logging(level: str = "INFO"):
    logger = logging.getLogger("ArchMusic")
    if logger.handlers:
        return logger
    logger.setLevel(getattr(logging, level.upper(), logging.INFO))
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s", "%H:%M:%S"))
    logger.addHandler(handler)
    return logger
