import os
from pathlib import Path
import logging

# Lee la ruta desde una variable de entorno
FILE_PERSIST_PATH = Path(os.getenv("FILE_PERSIST_PATH", "FILE_PERSIST"))
FILE_PERSIST_PATH.mkdir(parents=True, exist_ok=True)

logger = logging.getLogger(__name__)

def save_file(filename: str, contents: bytes) -> str:
    file_path = FILE_PERSIST_PATH / filename
    try:
        with open(file_path, "wb") as f:
            f.write(contents)
        logger.info(f'Archivo guardado: {file_path}')
    except Exception as e:
        logger.error(f'Error al guardar el archivo {filename}: {e}')
        raise
    return str(file_path)

def backup_file(filename: str, contents: bytes) -> None:
    backup_path = FILE_PERSIST_PATH / f"backup_{filename}"
    try:
        with open(backup_path, "wb") as f:
            f.write(contents)
        logger.info(f'Backup del archivo creado: {backup_path}')
    except Exception as e:
        logger.error(f'Error al crear el backup del archivo {filename}: {e}')
        raise
