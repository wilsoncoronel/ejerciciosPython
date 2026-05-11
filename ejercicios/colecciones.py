from collections import Counter, defaultdict, namedtuple, deque
numeros =[8,2,3,41,5,7,2,3,10]

print(Counter(numeros))
frase = "Al pan, pan, y al vino, vino"
print(Counter(frase.split()))

serie = Counter([1,1,1,1,1,1,2,3,3,3,4,7,8,88,88,1])

print(serie.most_common())

mi_dic = {"uno":"verde","dos":"azul", "tres":"rojo"}
mi_dic = defaultdict(lambda: "nada", mi_dic)
print(mi_dic["cuatro"])
print(mi_dic[""])
'''
mi_tupla = (5,11,18)
print(mi_tupla[1])

Persona = namedtuple('Persona', ['nombre','edad'])
ariel = Persona('Ariel',40,80)
print(ariel[1])

mi_diccionario = defaultdict()'''

mi_diccionario = {"edad", 44}
mi_diccionario = defaultdict(lambda: "Valor no hallado", mi_diccionario)
print(mi_diccionario["edad"])

