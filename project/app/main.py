from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from app.api.endpoints import router as api_router
from app.persistence.database import engine, Base
from app.utils.logging import setup_logging
from app.ui.templates import get_index_template
from dotenv import load_dotenv

setup_logging()

load_dotenv()

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(api_router)

@app.get('/healthcheck/')
async def healthcheck():
    return {'status': 'active'}

@app.get('/', response_class=HTMLResponse)
async def main():
    content = get_index_template()
    return HTMLResponse(content=content)
