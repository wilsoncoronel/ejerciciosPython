'''import os
ruta = "C:\\Users\\DOOMSLAYER\\Desktop\\proyectos\\python\\docs\\pruebas.txt"
archivo = os.path.basename(ruta)
print(archivo)
directorio = os.path.dirname(ruta)
print(directorio)
mi_ruta = os.path.split(ruta)
print(mi_ruta)'''
'''from pathlib import Path
carpeta = Path("C:\\Users\\DOOMSLAYER\\Desktop\\proyectos\\python\\docs\\pruebas.txt")
mi_archivo = carpeta / 'otro_archivo.txt'
archivo = open(mi_archivo, "r")
print(archivo.read())

print(carpeta.read_text())
print(carpeta.name)
print(carpeta.suffix)
print(carpeta.stem)
print(carpeta.exists())
if not carpeta.exists():
    print("No existe")
else:
    print("Si existe")'''

'''from pathlib import Path

base = Path.home()
guia = Path(base,'Europa','Espania',Path('Barcelona', 'Sagrada Familia'))

print(guia.parent.parent)

guia = Path(Path.home() / "Europa")

for txt in Path(guia).glob("*.txt"):
    print(txt)

en_europa = guia.relative_to(Path('Europa'))
en_espana = guia.relative_to(Path("Europa", "España"))
print(en_europa)
print(en_espana)'''

from os import system

