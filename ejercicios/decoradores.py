'''def cambiar_letras(tipo):
    def mayuscula(texto):
        print(texto.upper())

    def minuscula(texto):
        print(texto.lower())
    if tipo == "may":
        return mayuscula
    elif tipo == "min":
        return minuscula
    
operacion = cambiar_letras("min")
operacion("palabra")'''
def decorar_saludo(funcion):
    def otra_funcion(palabra):
        print("Hola")
        funcion(palabra)
        print("Adios")
    
    return otra_funcion


def mayuscula(texto):
    print(texto.upper())

def minuscula(texto):
    print(texto.lower())

mayuscula_decorada = decorar_saludo(mayuscula)
minuscula_decorada = decorar_saludo(minuscula)

mayuscula_decorada("DOTNET")

