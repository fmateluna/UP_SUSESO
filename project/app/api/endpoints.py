from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from app.services.file_service import save_file, backup_file
from app.persistence.database import SessionLocal
from app.models.models import RegistroLicenciasMedicas
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post('/uploadfile/')
async def upload_file(file: UploadFile = File(...), db: SessionLocal = Depends()):
    contents = await file.read()
    db_file = RegistroLicenciasMedicas(nombre_archivo=file.filename, contenido_archivo=contents)
    db.add(db_file)
    db.commit()
    db.refresh(db_file)
    logging.info(f'Archivo subido: {file.filename}')
    return {'filename': file.filename}

@router.post('/uploadfilex/')
async def upload_file(file: UploadFile = File(...), db: SessionLocal = Depends()):
    try:
        logger.debug(f'Recibido archivo: {file.filename}')
        contents = await file.read()
        logger.debug(f'Recibido archivo: {file.filename}')
        
        file_path = save_file(file.filename, contents)
        backup_file(file.filename, contents)
        
        db_file = RegistroLicenciasMedicas(
            nombre_archivo=file.filename,
            contenido_archivo=contents,
            file_path=file_path
        )
        
        db.add(db_file)
        db.commit()
        db.refresh(db_file)
        
        logger.info(f'Archivo subido y respaldado: {file.filename}')
        
        return {'filename': file.filename}
    
    except Exception as e:
        logger.error(f'Error en la carga del archivo {file.filename}: {e}')
        raise HTTPException(status_code=500, detail="Error al cargar el archivo.")
