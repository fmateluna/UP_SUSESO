from datetime import datetime, timedelta
from fastapi import FastAPI, APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.file_service import save_file
from app.utils.file_processor import FileProcessor 
from app.persistence.database import SessionLocal, get_db
from app.models.models import RegistroLicenciasMedicas
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer
import logging
from app.services.file_service import save_file

SECRET_KEY = "ARCHIVO_SUSESO"  #TODO: Leer de variables de entorno
ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

router = APIRouter()

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        usuario = payload.get("Usuario")
        origen = payload.get("Origen")
        logger.info(f"Usuario: {usuario}, Origen: {origen}")
        if usuario is None or origen is None:
            logger.error(f'Claims vacios!! {usuario} {origen}')
            raise HTTPException(status_code=401, detail="Token inválido o claims faltantes")
        return payload
    except JWTError:
        logger.error(f'Token no valido {token}')
        raise HTTPException(status_code=401, detail="Token inválido o expirado")

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

@router.post("/token")
async def login():
    access_token_expires = timedelta(minutes=10)
    access_token = create_access_token(
        data={"Usuario": "root", "Origen": "Oficina23"}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.post('/uploadfile/')
async def upload_file(file: UploadFile = File(...), db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    payload = verify_token(token)
    try:
        contents = await file.read()
        file_path = save_file(file.filename, contents)
        logger.info(f"Archivo respaldado en : {file_path}, desde: {payload}")        
    except Exception as e:
        logger.error(f'Error en la respaldar del archivo {file.filename}: {e}')
    
    extracted_text=''
    try:
        extracted_text = FileProcessor.extract_text(contents, file.filename)
    except Exception as e:
        logger.error(f'No fue posible extraer texto desde {file.filename}: {e}')
    
    db_file = RegistroLicenciasMedicas(
        nombre_archivo=file.filename,
        contenido_archivo=contents,
        informacion_archivo=extracted_text,
        autor=payload.get("Usuario"),
        oficina=payload.get("Origen"),
    )
    db.add(db_file)
    db.commit()
    db.refresh(db_file)
    logging.info(f'Archivo subido: {file.filename}')
    
    
    
    return {'filename': file.filename}