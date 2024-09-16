from sqlalchemy import Column, Integer, String, LargeBinary

from app.persistence.database import Base,DATABASE_URL,engine

    
class RegistroLicenciasMedicas(Base):
    __tablename__ = 'registro_licencias_medicas'
    id = Column(Integer, primary_key=True, index=True)
    nombre_archivo = Column(String, index=True)
    contenido_archivo = Column(LargeBinary)
    
Base.metadata.create_all(bind=engine)