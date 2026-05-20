import os, re, datetime, time
'''Para lograrlo vas a usar el módulo os para abrir e iterear por el directorio,
y las expresiones regulares para encontrar el formato de número de serie correcto.

A los fines de este ejercicio, estas son las condiciones de formato que deben cumplir los hallazgos:
- [N] + [tres carateres de texto] + [-] + [5 números]'''
from pathlib import Path
lista_archivos_dir=[]
lista_series = {}
patron = re.compile(r"N\w{3}-\d{5}")
for ruta, carpetas, archivos in os.walk("."):
    if(any(f.is_file() for f in Path(ruta).iterdir())):
        if(ruta != '.' or ruta != ".\proyecto9" ):
            lista_archivos_dir.append(ruta)

inicio = time.time()
for index,rutaArchivo in enumerate(lista_archivos_dir):
    if index >= 2:
        carpeta = Path(lista_archivos_dir[index])
        for archivo in carpeta.glob('*.txt'):
            mi_archivo = open(f"{carpeta}\\{archivo.name}", "r")
            archi_leido = mi_archivo.read()
            resultado = re.search(patron, archi_leido)
            if resultado:
                lista_series[archivo.name] = resultado.group()


final = time.time()
print("----------------------------------------------------")
print(f"Fecha actual: {datetime.date.today()}")
duracion = final -inicio
print("ARCHIVO          NRO. SERIE")
print("------           ----------")
for archivoName, serial in lista_series.items():
    print(f"{archivoName}    {serial}")

print(f"Números encontrados: {len(lista_series)}")
print(f"Duración de la búsqueda: {duracion}")


