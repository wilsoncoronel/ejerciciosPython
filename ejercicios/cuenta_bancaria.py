lista_opciones ={"1": "Ver info Cliente", "2": "Depositar", "3": "Retirar", "4": "Salir"}
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    
class Cliente(Persona):
    def __init__(self, nombre, apellido,cuenta, balance):
        self.nombre = nombre
        self.apellido = apellido
        self.cuenta = cuenta
        self.balance = balance

    def DatosCliente(self):
        print(f"{self.nombre} {self.apellido}")
        print(f"Cuenta: {self.cuenta} / Balance: {self.balance}")

    def Depositar(self, cantidad: int):
        self.balance += cantidad
        
    def Retirar(self, cantidad: int):
        if int(self.balance) < cantidad:            
            print("No se puede retirar un valor mayor a su balance!!")
        else:
            self.balance -= cantidad

def Presentacion():
    print("Bienvenido")

def CrearCliente():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    cuenta = input("Ingrese el numero de cuenta: ")
    balance = 0
    ListarOpciones()
    cliente1 = Cliente(nombre, apellido, cuenta, balance)
    return cliente1
def Opciones(opc, cliente):
    while opc != "4":
        match opc:
            case "1":
                cliente.DatosCliente()
            case "2":
                valor = input("Ingrese el valor: ")
                cliente.Depositar(int(valor))
            case "3":
                valor = input("Ingrese el valor: ")
                cliente.Retirar(int(valor))
            case _:
                print("Opcion no valida")
        ListarOpciones()
        opc = input("Seleccione una opcion: ")

def Main():
    Presentacion()
    cliente = CrearCliente()
    opc = input("Ingrese una opcion: ")
    Opciones(opc, cliente)
def ListarOpciones():
    global lista_opciones
    for opcion, val in lista_opciones.items():
        print(f"{opcion}: {val}")            
Main()
        
