
'''lista_nombre =['Wilson', 'Ivan', 'Leo', 'Hugo', 'Alcides', 'Siegfrid', 'Maximo', 'Abrahan', 'Aturo', 'Edward', 'Alphonse']
dic = {"clave1": "A", "clave2":"B", "clave3":"C"}
for nombre in lista_nombre:
    print(f"El nombre {nombre} esta en la posicion: {lista_nombre.index(nombre)}")

for letra in lista_nombre[0]:
    print(letra)

for objeto in [[2,4], [3,5], [1,1]]:
    print(objeto)

for elemt1, elemt2 in [[2,4], [3,5], [1,1]]:
    print(elemt1)
    print(elemt2)

for item in dic.items():
    print(item)'''

'''monedas = 5
while monedas > 0:
    print(f"Tengo {monedas} monedas")
    monedas = monedas -1'''

'''mi_lista = ["a", "b", "c"]

mis_elementos = list(enumerate(mi_lista))
print(mis_elementos)
'''

'''nombres = ["Wilson", "Hugo", "Maximo"]
edades = [64, 29, 42]
ciudades = ["Lima", "Madrid", "Mexico"]

combinados = zip(nombres, edades, ciudades)
lista_combinados = list(zip(nombres, edades))
for objeto in combinados:
    print(objeto)

print(lista_combinados)'''

'''lista = [58, 50,97,100]

print(f"El menor es {min(lista)} y el mayor es {max(lista)}")

nombres = ["Wilson", "Hugo", "Maximo"]
print(min(nombres))

nombre = "Carlos"
print(min(nombre.lower()))
dic = {"c1":45, "c2":11}
print(min(dic))'''

'''from random import *

aleatorio = randint(1,50)
print(aleatorio)

aleatorio2 = random()
print(aleatorio2)

colores = ["azul", "amarillo", "rojo"]
aleatorio3 = choice(colores)
print(aleatorio3)

numeros = list(range(5,50, 5))
shuffle(numeros)
print(numeros)'''

'''palabra = 'python'

lista =[letra for letra in palabra]

for letra in palabra:
    lista.append(letra)

print(lista)

lista2 = [n for n in range(0,21,2)]
print(lista2)

lista3 = [n*2 for n in range(0,21,2)]
print(lista3)

lista4 = [n if n * 2> 10 else 'no' for n in range(0,21,2)]
print(lista4)

pies = [10,20,30,40,50]
metros =[m/3.281 for m in pies]
print(metros)'''



'''def misum(a, b):
    return a+b



def mimul():
    rest1 = misum(10,34)
    return rest1 * 10
resultado  = mimul()
print(resultado)

def mi_fun(*args):
    total =0
    for arg in args:
        total += arg
    return total

print(mi_fun(1,69,3))
'''
'''primero los argumentos, luego los *args, y por ultimo **kwargs'''
def prueba(num1, num2,*args,**kwargs):
    print(f"El primer valor es {num1}")
    print(f"El segundo valor es {num2}")
    for arg in args:
        print(f"arg es igual a {arg}")

    for clave, valor in kwargs.items():
        print(f"{clave} es igual a {valor}")
        
lista_args =[23,123,255,2654]
dic_kwargs = {"x":3,"y":4,"z":20}
prueba(5,11, lista_args, dic_kwargs)