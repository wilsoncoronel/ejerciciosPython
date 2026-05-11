import os
import shutil
#import send2trash

print(os.getcwd())
archivo = open("curso.txt", "w")
archivo.write("Texto de pruebas")
archivo.close()

#print(os.listdir())
archivo.close()

#shutil.move("curso.txt", "C:\\Users\\DOOMSLAYER\\Desktop\\proyectos\\python\\ejercicios\\Recetas")
'''
os.unlink()
os.rmdir()
shutil.rmtree()'''

#send2trash.send2trash("curso.txt")
ruta = 'C:\\Users\\DOOMSLAYER\\Desktop\\proyectos\\python\\ejercicios'
for carpeta, subcarpetas, archivos in os.walk(ruta):
    print(f"En la carpeta: {carpeta}")
    print(f"Las carpetas son: ")
    for sub in subcarpetas:
        print(f"\t{sub}")
    print(f"Los archivos son: ")
    for archivo in archivos: