def al_cuadrado():
    numero = int(input("Ingrese un número: "))
    resultado = numero * numero
    print(f"EL cuadrado de {numero} es {resultado}")
    print("Gracias por clacular el cuadrado")
try:
    al_cuadrado()
except ValueError:
    print("Ese no es un numero!!")
except:
    print("Ocurrió un error inesperado")
else:
    print("El programa se ejecutó correctamente")
finally:
    print("Fin del programa")

def pedir_numero():
    while True:
        try:
            numero = int(input("Ingrese un número: "))
        except:
            print("Ese no es un número válido. Intente de nuevo.")
        else:
            print("Ingresaste el numero ", numero)
            break
    print("Gracias")
pedir_numero()
 