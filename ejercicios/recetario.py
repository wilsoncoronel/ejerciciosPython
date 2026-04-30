import os
import shutil
import subprocess
from pathlib import Path

from colorama import Fore, Style, init
init()
ruta= Path("C:\\Users\\DOOMSLAYER\\Desktop\\proyectos\\python\\ejercicios\\Recetas")
rutaActual=""
dic_opciones = {}
dic_archivos = {}
dic_opciones_archivos = {"1":"Abrir", "2":"Crear","3":"Sobreescribir", "4":"Eliminar"}
dic_opciones_carpetas = {"1":"Ver Carpetas", "2":"Crear Nueva Carpeta","3":"Eliminar Carpeta", "4":"Salir"}

def limpiar_pantalla():
    # 'cls' para Windows, 'clear' para Unix/Linux/macOS
    comando = 'cls' if os.name == 'nt' else 'clear'
    subprocess.run(comando, shell=True)

def MensajeInicio(ruta):
    limpiar_pantalla()
    print(f"{Fore.GREEN}Bienvenido al administrador de recetas.\nEstamos trabajando en esta direccion: {ruta}{Style.RESET_ALL}")
    
    CargarOpcionesCarpeta(False)
    global dic_opciones
    print(f"{Fore.YELLOW}Escoja una de las opciones de carpetas:{Style.RESET_ALL} ")
    opcCarpeta = RecorrerOpcionesCarpeta()

    if opcCarpeta == "1":
        VerCarpetas(ruta)
    elif opcCarpeta == "2":
        CrearNuevaCarpeta(ruta)
    elif opcCarpeta == "3":
        CargarOpcionesCarpeta(True)
        print("Escoge una carpeta a eliminar")
        opcCarpeta = input("Opcion: ")
        EliminarCarpeta(ruta,opcCarpeta)

def EliminarCarpeta(ruta, opcCarpeta):
    global dic_opciones
    rutaCarpetaEliminar = Path(ruta, dic_opciones[opcCarpeta])
    if os.path.exists(rutaCarpetaEliminar):
        shutil.rmtree(rutaCarpetaEliminar)
        print(rutaCarpetaEliminar)
        print(f"Carpeta eliminada")
    else:
        print(f"Carpeta no existe")

def CargarOpcionesCarpeta(imrpimir):
    carpetas = os.listdir(ruta)
    global dic_opciones
    
    if len(dic_opciones) == len(carpetas):
        for indice,carpeta in enumerate(carpetas):
            if imrpimir == True: 
                print(f"{indice+1}: {carpeta}")
    else:
        dic_opciones = {}
        for indice,carpeta in enumerate(carpetas):
            if imrpimir == True: 
                print(f"{indice+1}: {carpeta}")
                dic_opciones[f"{indice+1}"] = f"{carpeta}"

def CrearNuevaCarpeta(ruta):
    ListadoCarpetas()
    nuevaCarpeta = input("Ingrese el nombre de la nueva carpeta: ")
    os.mkdir(Path(ruta,nuevaCarpeta))
    print(f"Carpeta {nuevaCarpeta} creada!!")
    MensajeInicio(ruta)


def VerCarpetas(ruta):
    ListadoCarpetas()
    opcion= input("Opcion: ")
    if opcion == "":
        VerCarpetas(ruta)
    else:
        OpcionesCarpeta(opcion)

def ListadoCarpetas():
    print("Elija una de las categorias")
    global dic_opciones 
    dic_opciones = {}
    CargarOpcionesCarpeta(True)
    

def OpcionesCarpeta(opcion):
    print(f"Archivos actuales en la carpeta {dic_opciones[opcion]}")
    print("Escoja una opcion: ")
    rutaActual = Path(ruta, dic_opciones[opcion])
    archivos = os.listdir(rutaActual)
    if len(archivos) > 0:
        RecorrerArchivos(archivos)
    else:
        print("No existen archivos en la carpeta actual!!")
        CrearArchivo(rutaActual)
        archivos = os.listdir(rutaActual)
        RecorrerArchivos(archivos)

    opcion2= input("Opcion: ")
    if opcion2 == "":
        OpcionesCarpeta(opcion)
    else:
        ArchivoEscogidoOpciones(opcion2, rutaActual)

def RecorrerArchivos(archivos):
    for indice,archivo in enumerate(archivos):
            print(f"{indice+1}: {archivo}")
            dic_archivos[f"{indice+1}"] = f"{archivo}"
        
def ArchivoEscogidoOpciones(opcion2, rutaActual):
    print(f"{dic_archivos[opcion2]}")
    rutaCarpetaCreacion= rutaActual
    rutaActual = Path(rutaActual,dic_archivos[opcion2])
    print(rutaActual)
    opc = RecorrerOpcionesArchivos()
    if opc == "1":
        LeerArchivo(rutaActual)
    elif opc == "2":
        CrearArchivo(rutaCarpetaCreacion)
    elif opc == "3":
        SobreescribirArchivo(rutaActual)
    else:
        ElimnarArchivo(rutaActual)
    global ruta
    MensajeInicio(ruta)

'''Funciones de archivos'''
def CrearArchivo(rutaActual):
    nombreArchivo = input("Ingrese el nombre del archivo nuevo: ")
    rutaNuevoArchivo = Path(rutaActual,f"{nombreArchivo}.txt")
    nuevoarchivo = open(rutaNuevoArchivo, "x")
    nuevoarchivo.write("Nueva receta")
    nuevoarchivo.close()
    if Path(rutaNuevoArchivo).exists():
        print(f"Archivo {nombreArchivo}.txt creado con éxito!!")
    else:
        print("Error creando el archivo!!")

def LeerArchivo(rutaActual):
    archivo= open(rutaActual, "r")
    print(archivo.readlines())
    archivo.close()
    
def SobreescribirArchivo(rutaActual):
    archivo = open(rutaActual, "a")
    nuevoTexto = input("Ingrese un nuevo texto para la receta: ")
    archivo.write(f"\n{nuevoTexto}")
    archivo.close()
    LeerArchivo(rutaActual)
    print(archivo)

def ElimnarArchivo(rutaActual):
    if os.path.exists(rutaActual):
        os.remove(rutaActual)
        print(f"Archivo eliminado")
    else:
        print(f"Archivo no existe")

def RecorrerOpcionesArchivos():
    print("Escoja una opción:")
    for indice, opcion in dic_opciones_archivos.items():
        print(f"{indice} : {opcion}")
    opc = input("Opcion: ")
    return opc
    
def RecorrerOpcionesCarpeta():
    for indice, opcion in dic_opciones_carpetas.items():
        print(f"{indice} : {opcion}")
    opc = input("Opcion: ")
    return opc

MensajeInicio(ruta)