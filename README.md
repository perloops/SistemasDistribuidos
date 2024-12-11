# PROYECTO II 

En este proyecto nuestra problemática radica en que la UPIIZ necesita una aplicación para gestioanr la información de alumnos, profesores y mmaterias.
Esta aplicación permite la creación de crear, leer, actualizar y/o eliminar registro de estudiantes, profesores y materias.

## Objetivo
Crear una API RESTful que permita gestionar la información de una escuela, utilizando FastAPI como framework, MongoDB como base de datos NoSQL y AWS S3 como almacenamiento de archivos.


## Tecnologías usadas
- Python
- Visual Studio Code
- Mongo DB
- FastAPI
- AWS S3


### ¿Cómo funciona?
Módulos utilizados:
  ```python
from fastapi import FastAPI, File, UploadFile, HTTPException, Form, Depends
from pathlib import Path
import shutil
from pydantic import BaseModel
from motor import motor_asyncio
import boto3
from botocore.exceptions import NoCredentialsError
from datetime import datetime, timedelta
import uuid
from typing import Optional, List, Annotated
from fastapi.security import OAuth2AuthorizationCodeBearer, OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.exceptions import HTTPException
from jose import jwt
  ```

Configuración de conexión con MongoDB:
  ```python
MONGO_URI = "mongodb://localhost:27017"
cliente = motor_asyncio.AsyncIOMotorClient(MONGO_URI)
db = cliente["Escuela"]  
  ```

Configuración de cliente S3:
  ```python
s3 = boto3.client('s3')
BUCKET_NAME = "sistemas-distribuidos-upiiz-departamental2"  
  ```

Colecciones:
  ```python
alumnos_collection = db["Alumnos"]
materias_collection = db["Materias"]
profesores_collection = db["Profesores"]
calificacions_collection = db["Calificaciones"]  
  ```

Objeto para interactura con FastAPI:
  ```python
app = FastAPI()  
  ```

Ruta de almacenamiento de imágenes:
  ```python
IMAGES_DIR = Path("img")
IMAGES_DIR.mkdir(exist_ok=True)  # Crea la carpeta si no existe  
  ```

dhdhdhhrlos.
  ```python
  
  ```

dhdhdhhrlos.
  ```python
  
  ```
Creamos una función de llamada `obtener_datos_pokemon` que va a recolector datos como nombr.
  ```python
def obtener_datos_pokemon(pokemon_id):
    try:
        response = requests.get(f"{BASE_URL}{pokemon_id}")
        if response.status_code == 200:
            datos = response.json()
            nombre = datos["name"].capitalize()
            tipos = [tipo["type"]["name"].capitalize() for tipo in datos["types"]]
            estadisticas = {stat["stat"]["name"]: stat["base_stat"] for stat in datos["stats"]}
            imprimir_datos_pokemon(nombre, tipos, estadisticas)
        else:
            print(f"Error al obtener el Pokémon {pokemon_id}: {response.status_code}")
    except requests.RequestException as e:
        print(f"Excepción al obtener el Pokémon {pokemon_id}: {e}")
   ```

Creamos una función `imprimir_datos_pokemon` para poder mostrar las características.
  ```python
 def imprimir_datos_pokemon(nombre, tipos, estadisticas):
    print(f"Nombre: {nombre}")
    print(f"Tipo: {', '.join(tipos)}")
    print("Estadísticas:")
    print(f"  HP: {estadisticas.get('hp', 'N/A')}")
    print(f"  Ataque: {estadisticas.get('attack', 'N/A')}")
    print(f"  Defensa: {estadisticas.get('defense', 'N/A')}")
    print(f"  Ataque especial: {estadisticas.get('special-attack', 'N/A')}")
    print(f"  Defensa especial: {estadisticas.get('special-defense', 'N/A')}")
    print(f"  Velocidad: {estadisticas.get('speed', 'N/A')}")
    print("-" * 40)
  ```

Por último tenemos nuestra función `Main`, la cual se encarga de darle funcionamiento a nuestro código.
```python
def main():
    cantidad_pokemon = 50
    hilos = []
    for pokemon_id in range(1, cantidad_pokemon + 1):
        hilo = threading.Thread(target=obtener_datos_pokemon, args=(pokemon_id,))
        hilos.append(hilo)
        hilo.start()

    for hilo in tqdm(hilos, desc="Obteniendo datos de Pokémon"):
        hilo.join()
  ```


#### Integrantes:
- Perla Patricia Gómez Correa
- Karla Guadalupe Rocha Quezada
