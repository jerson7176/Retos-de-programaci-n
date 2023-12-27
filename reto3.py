# * Escribe un programa que imprima los 50 primeros números de la sucesión
#  * de Fibonacci empezando en 0.
#  * - La serie Fibonacci se compone por una sucesión de números en
#  *   la que el siguiente siempre es la suma de los dos anteriores.
#  *   0, 1, 1, 2, 3, 5, 8, 13...

n1 = 0
n2 = 1
while n2 <50:
    print(n1,n2,end=",")
    n1 += n2
    n2 += n1