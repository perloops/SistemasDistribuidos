# PRÁCTICA MULTITHREADING

En este proyecto se implementó y simuló el funcionamiento de una restaurante mediante 'multithreading' en Python.

## ¿Qué es multithreading?
El multithreading en Python es la creación y gestión de varios subprocesos dentro de un programa, de modo que se ejecuten simultáneamente. esto permite la ejecución paralela de tareas.

## Tecnologías usadas
- Python
- Visual Studio Code



### ¿Cómo funciona?
Primero  lo que hicimos fue importar los siguientes módulos:
- Time: 'time.sleep' para suspender la ejecución del hilo. 
- Random: 'randome.choice' para retornar un elemento aleatorio del menú, y 'random.randint' para el tiempo de espera     del cliente.
- Multiprocessing: 'multiprocessing.JoinableQueue' para crear cola de almacenamiento de pedidos.
  ```python
  import time
  import random
  import multiprocessing


Después definimos lo que sería nuestro menú, del cual los clientes cuentan con 5 opciones de comida diferentes.
  ```python
  MENU = ["Pizza", "Pasta", "Ensalada", "Hamburguesa", "Sopa", "Camarones"]
  ```

Creamos una función de llamada 'Mesa' que representa las mesas de nuestro restaurante, donde se realiza el pedido de forma aleatoria, se agrega el pedido a la cola y se comienza un tiempo de espera del pedido.
  ```python
  def mesa(id, cola_pedidos):
    # Generar un pedido de comida aleatoria del menu
    pedido = random.choice(MENU)
    print(f'Mesa {id}: Pidio {pedido}')
    # Agregar el pedido a la cola para que un camarero lo atienda
    cola_pedidos.put((id, pedido))
    # Simular el tiempo de espera del cliente
    time.sleep(random.randint(1, 5))
   ```

Creamos una función 'Camarero' para poder obtener el pedido, prepararlo (simulando igual un tiempo de preparación) y entregarlo. Todo esto dentro de una sentencia de ciclo que se detiene si ya no tenemos más pedidos en espera.
  ```python
       def camarero(id, cola_pedidos, lock):
    while True:
        try:
            # Obtener el pedido de la cola
            mesa_id, pedido = cola_pedidos.get(timeout=1)  # Evitar bloqueo en espera
            # Preparar el pedido
            with lock:
                print(f'Camarero {id}: Preparando {pedido} para la mesa {mesa_id}')
            time.sleep(5)  # Simular tiempo de preparación
            # Entregar el pedido
            with lock:
                print(f'Camarero {id}: Entregando {pedido} a la mesa {mesa_id}')
            cola_pedidos.task_done()
        except:
            break  # Romper el bucle si la cola está vacía
  ```

Por último tenemos nuestra función principal, la cual se encarga de darle funcionamiento a nuestros restaurante, dónde se organiza la toma de pedidos, que todas las mesas hayan ordenado algo, que los camareros no choquen entre si y que una vez terminados nuestros pedidos se tenga todo el proceso.
```python
    def main():
    num_mesas = 5
    num_camareros = 3


    # Crear una cola para almacenar los pedidos de las mesas
    cola_pedidos = multiprocessing.JoinableQueue()

    # Crear y lanzar los hilos de las mesas
    mesas = []
    for i in range(num_mesas):
        p = multiprocessing.Process(target=mesa, args=(i + 1, cola_pedidos))
        mesas.append(p)
        p.start()

    # Esperar a que todas las mesas hayan realizado sus pedidos
    for p in mesas:
        p.join()

    # Crear un lock para evitar conflictos entre los camareros
    lock = multiprocessing.Lock()

     # Crear y lanzar los procesos de los camareros
    camareros = []
    for i in range(num_camareros):
        p = multiprocessing.Process(target=camarero, args=(i + 1, cola_pedidos, lock))
        camareros.append(p)
        p.start()

    # Esperar a que todos los camareros hayan completado sus tareas
    cola_pedidos.join()  # Esperar a que todos los pedidos sean atendidos

    for p in camareros:
        p.terminate()  # Terminar los procesos de los camareros una vez completados los pedidos

    print("Todos los pedidos han sido entregados.")
  ```


## Resultados
Una vez corrido todo el código, nuestro restaurante funcioando se vería algo así:
  ![Captura de resultados obtenidos]()

