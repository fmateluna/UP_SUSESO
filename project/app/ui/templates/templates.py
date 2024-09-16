import os

def get_index_template(page: str) -> str:
    # Establecer el path del template por defecto
    template_path = os.path.join(os.path.dirname(__file__), 'login.html')
    
    # Cambiar el path si la página es 'licencias'
    if page == 'licencias':
        template_path = os.path.join(os.path.dirname(__file__), 'index.html')
    
    # Leer el archivo
    try:
        with open(template_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"El archivo {template_path} no se encontró.")
    except IOError:
        raise IOError(f"Error al leer el archivo {template_path}.")

    