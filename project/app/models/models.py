from sqlalchemy import Column, Integer, String, LargeBinary
from app.persistence.database import Base

class RegistroLicenciasMedicas(Base):
    __tablename__ = 'licencias_medicas'
    id = Column(Integer, primary_key=True, index=True)
    nombre_archivo = Column(String, index=True)
    contenido_archivo = Column(LargeBinary)
    file_path = Column(String)  # New column for file path
