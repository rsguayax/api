Proyecto que genera un API con un método POST
Este proyecto es una API para encontrar el subarreglo máximo en un arreglo de números cuya suma sea igual a un número objetivo dado.

Objetivo.
- Encontrar el subarreglo más largo con un número objetivo dado

Framework
- Implementado con Django REST Framework.

Instalación
1. Clona el repositorio de github:
   git clone https://github.com/rsguayax/api.git

2. Navega al directorio del proyecto:
   cd principal

3. Crea un entorno virtual:
   python -m venv venv

4. Activación del entorno virtual:
   - venv\Scripts\activate

5. Instala las dependencias:
   pip install -r requirements.txt

6. Ejecuta las migraciones:(este paso fue necesario, ya que no me dejó ejecutar el proyecto sin antes correr este comando)
   python manage.py migrate

7. Ejecuta el servidor:
   python manage.py runserver

Test de la API
http://localhost:8000/api/subarray/

Es un método POST con una entrada similar a esta:

{
    "array": [1, -2, 1, 1, -1, 2, 4],
    "target": 3
}

Devuelve una respuesta como esta:
{
   "subarray": [1, 1, -1, 2]
}