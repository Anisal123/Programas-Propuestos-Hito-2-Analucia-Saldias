# 1
print ("Ejemplo 1 Concatenación:")

mensaje = "Hola curso"
espacio = " "
mensaje1 = "Hola estoy en el 3er semestre"
mensaje2 = "Mi curso es el 205" 
print (mensaje + espacio + mensaje1 + espacio + mensaje2)
separador = "--------------------"
print(separador)
#2
print ("Ejemplo 2:")
num1 = 30
num2 = 70
num3= 40
num4=50
num5=25
num6=30
num7=10
num8= 50
resultado1 = num1 + num2
resultado1 = str(resultado1)
print("Resultado 1 de 30+70 es = "+resultado1)

resultado2 = num3 + num4
resultado2 = str(resultado2)
print("Resultado 2 de 40+50 es = "+resultado2)

resultado3 = num5 + num6
resultado3 = str(resultado3)
print("Resultado 3 de 25+30 es = "+resultado3)

resultado4 = num7 + num8
resultado4 = str(resultado4)
print("Resultado 4 de 10+50 es = "+resultado4)
separador = "--------------------"
print(separador)
#3
print ("Ejemplo 3: Busqueda")
Frase_1 = "Hola Curso"
Frase_2 = "Hola estoy en 3er Semestre"
Frase_3 = "Mi curso es el 205"

busqueda_frase_1 = Frase_1.find("a")
busqueda_frase_2 = Frase_2.find("t")
busqueda_frase_3 = Frase_3.find("s")

print(busqueda_frase_1)
print(busqueda_frase_2)
print(busqueda_frase_3)

print(f"{Frase_2 == Frase_1}")

separador = "--------------------"
print(separador)