from sqlalchemy import Column, Integer, String, LargeBinary, DateTime, Text
from sqlalchemy.sql import func
from app.persistence.database import Base
from app.persistence.database import Base,DATABASE_URL,engine

class RegistroLicenciasMedicas(Base):
    __tablename__ = 'licencias_medicas'
    
    id = Column(Integer, primary_key=True, index=True)
    nombre_archivo = Column(String, index=True)
    contenido_archivo = Column(LargeBinary)
    informacion_archivo = Column(Text) 
    autor = Column(String)  
    oficina = Column(String)  
    fecha = Column(DateTime, server_default=func.now())  

Base.metadata.create_all(bind=engine)