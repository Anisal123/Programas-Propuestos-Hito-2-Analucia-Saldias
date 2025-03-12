#4.-Escribir un programa que pida al usuario una palabra y muestre por pantalla el número 
#de veces que contiene cada vocal.
cadena= input("Introduce una palabra: ")
vocales= "aeiou"
contador= {vocal: cadena.count(vocal)
           for vocal in vocales
           }
print(contador)