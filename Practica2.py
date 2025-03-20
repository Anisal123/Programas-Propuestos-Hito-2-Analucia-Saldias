
#Ejercicio 1: Escribir un programa que almacene las asignaturas de un curso (por ejemplo, 
#Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el 
#mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la 
#Lista.

asignaturas= [ 'Matematicas','Fisica','Quimica','Estructura de datos', 'Sistemas Operativos']
for asignatura in asignaturas: 
    print(f"Yo estudio {asignatura}")

separador = "--------------------"
print(separador)

#Ejercicio 2
parte1 = [1, 2, 8, 4, 7]
parte2 = [6, 3, 9, 5]
lista = parte1 + parte2
lista.sort()

print(lista)

separador = "--------------------"
print(separador)

#Ejercicio 3
lista = [6, 9, 3, 10, 7, 2, 1, 4, 8, 5]
lista.sort()
print(lista)

separador = "--------------------"
print(separador)

#Ejercicio4: Escribir un programa que pida al usuario una palabra y muestre por pantalla el número 
#de veces que contiene cada vocal.
cadena= input("Introduce una palabra: ")
vocales= "aeiou"
contador= {vocal: cadena.count(vocal)
           for vocal in vocales
           }
print(contador)

separador = "--------------------"
print(separador)

#Ejercicio 5: Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 
#65, 8, y muestre por pantalla el menor y el mayor de los precios.

precios=  [50, 75, 46, 22, 80, 65, 8 ]
precio_mas_bajo= min(precios)
precio_mas_alto=max(precios)
print(f"El precio mas bajo es {precio_mas_bajo}, y el precio mas alto es {precio_mas_alto}")

separador = "--------------------"
print(separador)

#Ejercicio 6: Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 
#'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si 
#la divisa no está en el diccionario.

divisas = {
    'Euro': '€', 
    'Dollar': '$', 
    'Yen': '¥'}
moneda= input("Ingrese la divisa que desea verificar: ").capitalize()
simbolo= divisas.get(moneda)
if simbolo!=None:
    print(f"El simbolo de la divisa es:{simbolo}")
else: 
    print(f"La moneda {moneda}no existe")
    
    separador = "--------------------"
print(separador)

#Ejercicio 7: Ingresar un vector de n elementos de tipo entero. Ordenar posteriormente el vector en 
#forma ascendente {5,3,6,4,8,1,9,2}

cantidad= int (input("Ingrese la cantidad de elementos que desean ordenar:"))
numeros= [ ]
for i in range(cantidad):
    numero= int(input("Ingrese un valor: "))
    numeros.append(numero)
    
numeros.sort()
print(numeros)

separador = "--------------------"
print(separador)

#Ejercicio 8: Escribir un programa que cree un diccionario vacío y lo vaya llenado con información 
#sobre una persona (por ejemplo, nombre, edad, sexo, teléfono, correo electrónico, etc.) que 
#se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del 
#diccionario.

persona={}
#FORMA 1 Atributos fijos

campos = ["Nombre", "Edad", "Sexo", "Teléfono", "Correo Electrónico"]

for campo in campos:
    valor =  input(f"Ingresa el valor para {campo}: ")
    persona[campo] = valor
    print("Diccionario actualizado:", persona) 


#FORMA 2 añadiendo atributos
#while True:
 #   atributo = input("Ingresa el atributo: ")
  #  valor = input(f"Ingresa el valor para {atributo}: ")
  #  persona[atributo] = valor
  #  print(persona)
    
separador = "--------------------"
print(separador)

#Ejercicio 9: Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, 
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

separador = "--------------------"
print(separador)

#Ejercicio 10

tupla= ('a','e','i','o','u')
print(tupla)

separador = "--------------------"
print(separador)

#Ejercicio 11
parte1 = [11,12]
parte2 = [7,8,9,10]
parte3 = [1,2,3,4,5,6]
lista = parte1 + parte2 +parte3
lista.sort()

print(lista)

separador = "--------------------"
print(separador)

#Ejercicio  12
numeros_vertical = [7, 6, 5, 4, 3, 2, 1]
numeros_horizontal = []
for numero in numeros_vertical:
    numeros_horizontal.append(numero)

print("Lista horizontal:", numeros_horizontal)
    