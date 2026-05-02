'''def mi_funcion():
    lista = []
    for x in range(1,5):
        lista.append(x*10)
    return lista

def mi_generador():
    for x in range(1,5):
        yield x*10

print(mi_funcion())
print(mi_generador())

g = mi_generador()
print(next(g))
print(next(g))

print("Hola esta es una linea que no hace nada")
print(next(g))'''


'''def mi_generador():
    x =1
    yield x
    x += 1
    yield x

    x += 1
    yield x

g = mi_generador()
print(next(g))
print(next(g))
print(next(g))'''

'''def mi_generador(seguir):
    x =0
    while seguir== True:
        x = x+1
        yield x


generador = mi_generador(True)
print(next(generador))
print(next(generador))
print(next(generador))'''

'''def mi_generador(seguir):
    x =7
    multiplo = 1
    while seguir== True:
        x = multiplo*7
        multiplo += 1
        yield x


generador = mi_generador(True)
print(next(generador))
print(next(generador))
print(next(generador))'''

def perder_vida():
    vida = 3
    while vida > 0:
        yield  f"Te queda{'n' if vida >1 else ''} {vida} vida{'s' if vida >1 else ''}"
        vida -= 1
    else:
        yield "Game over"

generador = perder_vida()
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))

