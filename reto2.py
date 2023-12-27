# * Escribe una función que reciba dos palabras (String) y retorne
#  * verdadero o falso (Bool) según sean o no anagramas.
#  * - Un Anagrama consiste en formar una palabra reordenando TODAS
#  *   las letras de otra palabra inicial.
#  * - NO hace falta comprobar que ambas palabras existan.
#  * - Dos palabras exactamente iguales no son anagrama.


def son_anagramas (palabra1,palabra2):
    palabra1_organizada = sorted(palabra1)
    palabra2_organizada = sorted(palabra2)

    if palabra1 == palabra2:
        return False
    
    return palabra1_organizada == palabra2_organizada


palabra1 = "amor"
palabra2 = "roma"
resultado = son_anagramas(palabra1,palabra2)
print(resultado)