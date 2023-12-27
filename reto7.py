# Crea un programa se encargue de transformar un número
# decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.

numero_decimal = 27

if numero_decimal == 0:
    resultado_binario = "0"
else:
    resultado_binario = ""


while numero_decimal > 0:
    residuo = str (numero_decimal % 2)
    resultado_binario = residuo + resultado_binario
    numero_decimal //= 2

print(f"El número  binario correspondiente es: {resultado_binario}")

        