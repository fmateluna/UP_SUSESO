### Instrucciones para ejecutar la aplicación FastAPI ###

1. Crear un entorno virtual:
python -m venv venv

2. Activar el entorno virtual:
- En Windows: .\venv\Scripts\activate
- En Unix o MacOS: source venv/bin/activate

3. Instalar dependencias:
pip install -r requirements.txt

4. Ejecutar la aplicación con Uvicorn:
uvicorn app.main:app --reload

5. Abrir el navegador y acceder a:
- Interfaz web para cargar archivos: http://127.0.0.1:8000/
- Endpoint para subir archivos: http://127.0.0.1:8000/uploadfile/
- Health check: http://127.0.0.1:8000/healthcheck/

pip install python-multipart
pip install pytesseract pillow PyMuPDF
pip install python-jose[cryptography] python-dotenv

cd project
pip install -r requirements.txt
set FILE_PERSIST_PATH=FILE_PERSIST
set LOG_PATH=log
set DATABASE_URL=postgresql://postgres:XXX@junction.proxy.rlwy.net:34564/railway
uvicorn app.main:app --reload

curl -X 'POST' \
  'http://localhost:8000/uploadfile/' \
  -H 'Authorization: Bearer 
eyJhbGciOiJIUzI1NiJ9.eyJVc3VhcmlvIjoiRmVybmFuZG8iLCJPcmlnZW4iOiJPZmljaW5hMjMifQ.Yp3fOoj9urZsTLttigYUhpLnlc43C8L0Onxac7MjN8E' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@/ruta/al/archivo.txt'
