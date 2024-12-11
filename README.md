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

Tenemos 6 modelos de datos, los cales son:
- Alumno:  ```id, nombre, apellido, fecha_nacimiento, direccion, foto ```
- Materias:  ```id, nombre, descripcion, profesor_id ```
- Profesor:  ```id, nombre, apellido, fecha_nacimiento, direccion, especialidad, materias_id ```
- calificacion:  ```id, alumno_id, materia_id, calificacion ```
- Token:  ```access_token, token_type ```
- User:  ```username, role ```

Configuración de cliente OAuth2:
  ```python
SECRET_KEY = "my-secret"  # Cambiar por una clave más segura en producción
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")  
  ```

Diccionario de usuarios:
  ```python
users = {
    "admin": {"username": "admin", "password": "1234", "role": "admin"},
    "user": {"username": "user", "password": "1234", "role": "user"},
}

@app.get("/")
async def read_root():
    return {
        "message": "¡Bienvenido a la API de Ecuela!",
        "1": "Miguel Alejandro Rodríguez Cruz",
        "2": "Carlos Omar Fernández Casillas",
        "3": "Axel Giovanni Ojeda Hernández",
        "4": "Perla Patricia Gómez",
        "5": "Karla Guadalupe Rocha Quezada",
        "6": "Desire Castañeda García",
    }  
  ```

Para los alumnos, profesores, materias y calificaciones se implementa su CRUD respectivamente.
- Crear  ```@app.post()   ```
- Leer  ```@app.get()   ```
- Actualizar  ```@app.put()   ```
- Eliminar  ```@app.delete()   ```

Las materias son asignadas a profesores y estos pueden tener varias materias a la vez.
Los alumnos son inscritos a la materias  pueden estar inscritos en varias materias a la vez.
Las calificaciones están asociadas a un alumno y una materia específica.



#### Integrantes:
- Carlos Omar Fernández Casillas
- Miguel Alejandro Rodríguez Cruz
- Desireé Castañeda García
- Axel Giovanni Ojeda Hernández
- Perla Patricia Gómez Correa
- Karla Guadalupe Rocha Quezada
