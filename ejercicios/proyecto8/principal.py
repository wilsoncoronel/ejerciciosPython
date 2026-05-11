from numeros import generar_turnos_farmacia
def turno():
    yield from generar_turnos_farmacia(True)
    

def mi_decorador(funcion):
    def otra_funcion():
        print("Turno asigando:")
        for t in turno():
            yield t
            print("Espere a ser atendido...")
    return otra_funcion

turno = mi_decorador(turno)
gen = turno()
print(next(gen))