def generar_turnos_farmacia():
    turno = 1
    while True:
        yield f"F{turno}"
        turno += 1


def generar_turnos_perfumeria():
    turno = 1
    while True:
        yield f"P{turno}"
        turno += 1

def generar_turnos_cosmetica():
    turno = 1
    while True:
        yield f"C{turno}"
        turno += 1