#8.-Escribir un programa que cree un diccionario vacío y lo vaya llenado con información 
#sobre una persona (por ejemplo, nombre, edad, sexo, teléfono, correo electrónico, etc.) que 
#se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del 
#diccionario.

persona={}
#FORMA 1 Atributos fijos

# campos = ["Nombre", "Edad", "Sexo", "Teléfono", "Correo Electrónico"]

# for campo in campos:
#     valor =  input(f"Ingresa el valor para {campo}: ")
#     persona[campo] = valor
#     print("Diccionario actualizado:", persona) 


#FORMA 2 añadiendo atributos
while True:
    atributo = input("Ingresa el atributo: ")
    valor = input(f"Ingresa el valor para {atributo}: ")
    persona[atributo] = valor
    print(persona)
