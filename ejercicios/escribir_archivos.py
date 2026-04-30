archivo = open("C:\\Users\\DOOMSLAYER\\Desktop\\proyectos\\python\\ejercicios\\Prueba.txt", 'w')
'''archivo.write("Soy una nueva linea\n")
archivo.write("Soy una segunda linea")'''

lista = ["hola", 'mundo', 'aqui', 'estoy']
for p in lista:
    archivo.writelines(p + '\n')


archivo.close()
