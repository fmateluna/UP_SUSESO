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