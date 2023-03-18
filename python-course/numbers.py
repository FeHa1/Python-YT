# este termino ¨input()¨ toma un caracter de lo que tipe el usuario en la consola. 
# eneste caso lo almacene en una variable llamada ¨age¨.
age = input("Insert your age: ")
# si quiero puedo editar el resultado usando otra variable.
# Pero aca me va a saltar error poque estoy tratando de sumar un texto con un numero.
#new_age = age + 5 #aca estoy usando Snake Case porque lo separo por ¨_¨. (Lo comente para que no me lo tomara cuando lo ejecutara)

# la manera correcta de hacerlo seria esta:
new_age = int(age) + 5
print(new_age)


