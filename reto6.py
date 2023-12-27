#  * Crea un programa que invierta el orden de una cadena de texto
#  * sin usar funciones propias del lenguaje que lo hagan de forma automática.
#  * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"


saludo = "Hola mundo"
saludo_invertido = ""
for letra in saludo:
    saludo_invertido = letra + saludo_invertido
print(saludo_invertido)