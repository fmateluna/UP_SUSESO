import io
from PIL import Image
import pytesseract
import fitz  # PyMuPDF
from typing import Union

class FileProcessor:
    @staticmethod
    def detect_file_type(file_content: bytes, file_name: str) -> str:
        if file_name.lower().endswith('.pdf'):
            return 'pdf'
        elif file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
            return 'image'
        elif file_name.lower().endswith(('.txt')):
            return 'text'
        else:
            raise ValueError("Tipo de archivo no soportado")
    
    @staticmethod
    def extract_text_from_pdf(file_content: bytes) -> str:
        pdf_document = fitz.open(stream=file_content, filetype='pdf')
        text = ""
        for page in pdf_document:
            text += page.get_text()
        return text

    @staticmethod
    def extract_text_from_image(file_content: bytes) -> str:
        image = Image.open(io.BytesIO(file_content))
        text = pytesseract.image_to_string(image)
        return text

    @staticmethod
    def extract_text(file_content: bytes, file_name: str) -> str:
        file_type = FileProcessor.detect_file_type(file_content, file_name)
        
        if file_type == 'pdf':
            return FileProcessor.extract_text_from_pdf(file_content)
        elif file_type == 'image':
            return FileProcessor.extract_text_from_image(file_content)
        elif file_type == 'text':
            return file_content.decode('utf-8')
        else:
            raise ValueError("Tipo de archivo no soportado")
