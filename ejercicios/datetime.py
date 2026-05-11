'''En una variable llamada minutos, almacena únicamente los minutos de la hora actual.
Por ejemplo, si se ejecutara a las 20:43:17 de la noche, la variable minutos debe almacenar el valor 43'''

import datetime
ahora = datetime.datetime.now()
minutos = ahora.minute