


from fastapi import FastAPI, UploadFile, File, HTTPException, Depends
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, LargeBinary
from sqlalchemy.orm import sessionmaker
import logging

DATABASE_URL = 'postgresql://postgres:unbWdTGWwUCawrhXtISyNpsIGQDYucnU@junction.proxy.rlwy.net:34564/railway'

logging.basicConfig(level=logging.INFO)

app = FastAPI()

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class RegistroLicenciasMedicas(Base):
    __tablename__ = 'registro_licencias_medicas'
    id = Column(Integer, primary_key=True, index=True)
    nombre_archivo = Column(String, index=True)
    contenido_archivo = Column(LargeBinary)

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/uploadfileInit/')
async def upload_file(file: UploadFile = File(...), db: Session = Depends(get_db)):
    contents = await file.read()
    db_file = RegistroLicenciasMedicas(nombre_archivo=file.filename, contenido_archivo=contents)
    db.add(db_file)
    db.commit()
    db.refresh(db_file)
    logging.info(f'Archivo subido: {file.filename}')
    return {'filename': file.filename}

@app.get('/healthcheckInit/')
async def healthcheck():
    return {'status': 'active'}

@app.get('/TEST', response_class=HTMLResponse)
def main():
    content = """
        <html>
            <body>
                <h1>Subir Archivo</h1>
                <form action="/uploadfile/" enctype="multipart/form-data" method="post">
                    <input name="file" type="file">
                    <input type="submit">
                </form>
            </body>
        </html>
    """
    return HTMLResponse(content=content)
