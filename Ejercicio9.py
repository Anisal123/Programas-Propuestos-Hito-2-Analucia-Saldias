#9.-Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, 
#pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de 
#ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje 
#informando de ello.


frutas= {
    'Manzana': 50, 
    'Durzano': 40, 
    'Ciruelo': 80}
fruta =input("Ingrese la fruta que desea comprar: ")
cantidad= int(input(f"Ingrese la cantidad de Kg. de {fruta}para calcular el precio:"))
precio= frutas.get(fruta)
