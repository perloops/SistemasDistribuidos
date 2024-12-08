# PROYECTO II 

En este proyecto nuestra problemática radica en que la UPIIZ necesita una aplicación para gestioanr la información de alumnos, profesores y mmaterias.
Esta aplicación permite la creación de crear, leer, actualizar y/o eliminar registro de estudiantes, profesores y materias.

## Objetivo
Crear una API RESTful que permita gestionar la información de una escuela, utilizando FastAPI como framework, MongoDB como base de datos NoSQL y AWS S3 como almacenamiento de archivos.


## Tecnologías usadas
- Python
- Visual Studio Code
- Mongo DB


### ¿Cómo funciona?
Primero  lo que hicimos fue importar los siguientes módulos:
- `requests`, módulo que nos realizar enviar peticiones HTTP. 
- `threading` modulo que nos permite usar hilos para que se ejecuten múltiples operaciones simultáneamente en el mismo espacio.
- `tqdm` librería que utilizamos para mostrar barras de progreso en bucles e iterables, lo que permite hacer seguimiento del avance de tareas que requieren mucho tiempo.

  ```python
  import requests
  import threading
  from tqdm import tqdm 


Después conectamos de dónde se sacan los datos para leerlos.
  ```python
  BASE_URL = "https://pokeapi.co/api/v2/pokemon/"
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
