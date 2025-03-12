#7.- Ingresar un vector de n elementos de tipo entero. Ordenar posteriormente el vector en 
#forma ascendente {5,3,6,4,8,1,9,2}

cantidad= int (input("Ingrese la cantidad de elementos que desean ordenar:"))
numeros= [ ]
for i in range(cantidad):
    numero= int(input("Ingrese un valor: "))
    numeros.append(numero)
    
numeros.sort()
print(numeros)