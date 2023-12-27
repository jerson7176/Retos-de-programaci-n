#  * Crea una única función (importante que sólo sea una) que sea capaz
#  * de calcular y retornar el área de un polígono.
#  * - La función recibirá por parámetro sólo UN polígono a la vez.
#  * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
#  * - Imprime el cálculo del área de un polígono de cada tipo.

def area_poligono (poligono,b,h,l):
    if poligono == "triangulo":
        area = b * h / 2
        return area
    elif poligono == "cuadrado":
        area = l * l
        return area
    elif poligono == "rectangulo":
        area = b * h
        return area
    else:
        return "Poligono no encontrado"
    

b = 6
h = 6
l = 6

tipos_de_poligonos = ["triangulo","cuadrado","rectangulo"]

for tipo_de_poligonos in tipos_de_poligonos:
    resultado = area_poligono(tipo_de_poligonos,b,h,l)
    print(f"El area del {tipo_de_poligonos} es: {resultado}")