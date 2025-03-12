#6-Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 
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



