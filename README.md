# PRÁCTICA POKÉMONES 

En este proyecto se implementó el concepto 'multithreading' en Python para realizar tareas concurrentes, aprender a utilizar la biblioteca requests para realizar solicitudes HTTP a la PokeAPI, practicar la lectura y análisis de datos JSON y desarrollar habilidades para trabajar con hilos y sincronización en Python.

## ¿Qué es multithreading?
El multithreading en Python es la creación y gestión de varios subprocesos dentro de un programa, de modo que se ejecuten simultáneamente. esto permite la ejecución paralela de tareas.

## ¿Qué son las solicitudes PokeAPI?
Las solicitudes HTTP son mensajes que los clientes envían a los servidores para solicitar información o iniciar acciones. Son la principal forma de comunicación entre un cliente y un servidor.

## Tecnologías usadas
- Python
- Visual Studio Code



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
