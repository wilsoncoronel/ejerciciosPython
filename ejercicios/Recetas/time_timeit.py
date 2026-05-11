import time, timeit
def prueba_for(numero):
    lista=[]
    for num in range(1, numero+1):
        lista.append(num)
    return lista

def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista

inicio = time.time()
prueba_for(15)
final = time.time()
print(final - inicio)

inicio = time.time()
prueba_while(15)
final = time.time()
print(final - inicio)

declaracion = """
prueba_for(10)
"""
mi_setup = """
def prueba_for(numero):
    lista=[]
    for num in range(1, numero+1):
        lista.append(num)
    return lista
"""
duracion_for = timeit.timeit(declaracion, mi_setup, number=100000)
print(duracion_for)

declaracion_while = """
prueba_while(10)
"""
mi_setup_while = """
def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista
"""

duracion_while = timeit.timeit(declaracion_while, mi_setup_while, number=100000)
print(duracion_while)

