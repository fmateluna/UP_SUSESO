import os

def get_index_template() -> str:
    template_path = os.path.join(os.path.dirname(__file__), 'index.html')
    with open(template_path, 'r') as file:
        return file.read()