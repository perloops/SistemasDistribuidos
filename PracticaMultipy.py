import time
import random
import multiprocessing
from queue import Queue


# Definir las opciones de comida
MENU = ["Pizza", "Pasta", "Ensalada", "Hamburguesa", "Sopa", "Camarones"]

# Crear una clase Mesa que represente a cada mesa del restaurante

def mesa(id, cola_pedidos):
    # Generar un pedido de comida aleatoria del menu
    pedido = random.choice(MENU)
    print(f'Mesa {id}: Pidio {pedido}')
    # Agregar el pedido a la cola para que un camarero lo atienda
    cola_pedidos.put((id, pedido))
    # Simular el tiempo de espera del cliente
    time.sleep(random.randint(1, 5))

# Crear una función que representa el comportamiento de un camarero
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
            break  # Romper el bucle si la cola está vacíaa
   
# Función principal
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

if __name__ == "__main__":
    main()