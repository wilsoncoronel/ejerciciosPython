import re

texto = "Si necesitas ayuda llama al (658)-598-99767, este es un numero de nuestro programa de ayuda al ciudadano!!"
patron = "ayuda"

'''busqueda = re.search(patron, texto)
print(busqueda.span())
print(busqueda.start())
print(busqueda.end())

for hallazgo in re.finditer(patron,texto):
    print(hallazgo.span())

texto = 'llama al 554-655-4584 ya mismo'

#patron = r"\d\d\d-\d\d\d-\d\d\d\d"
patron = re.compile(r"(\d{3})-(\d{3})-(\d{4})")
resultado = re.search(patron, texto)

print(resultado.group(3))

clave = input("Introduce tu clave: ")
patron = r"\D{1}\w{7}"

resultado = re.search(patron, clave)
print(resultado)

texto = "No atendemos los lunes"
buscar = re.search("lunes|martes", texto)
print(buscar)'''

'''Crea una función llamada verificar_email para comprobar si una dirección de email es correcta,
que verifique si el email dado como argumento contiene "@" (entre el nombre de usuario y el dominio)
y finaliza en ".com" (aunque aceptando también casos que cuentan con un dominio adicional, 
tal como ".com.br" para el caso de un usuario de Brasil).

Si se encuentra el patrón, la función debe finalizar mostrando en pantalla el mensaje "Ok",
pero si detecta que la frase no contiene los elementos indicados, debe informarle al usuario
"La dirección de email es incorrecta" imprimiendo el mensaje.'''

def verificar_email(email):
    patron = r'\w+@\w+\.com\w*'
    if(re.search(patron, email)):
        print("Ok")
    else:
        print("La dirección de email es incorrecta")
        
verificar_email("wilson@hotmail.com")

def verificar_saludo(saludo):
    if(re.fullmatch(r"Hola|HOLA|hola",saludo)):
        print("Ok")
    else:
        print("No has saludado")
