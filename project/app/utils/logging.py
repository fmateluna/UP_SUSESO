import logging
import os
from pathlib import Path

# Lee la ruta del archivo de log desde una variable de entorno
LOG_PATH = Path(os.getenv("LOG_PATH", "log"))
LOG_PATH.mkdir(parents=True, exist_ok=True)

def setup_logging() -> None:
    log_file = os.path.join(LOG_PATH, "app.log")
    logging.basicConfig(
        level=logging.DEBUG,  # Puedes ajustar el nivel según tus necesidades
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
    logging.debug('Logging configurado.')
