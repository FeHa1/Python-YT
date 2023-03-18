# No podemos reasignar los elementos como en las listas.
# Son mucho mas rapidas que las listas 

x = (1, 2, 3) # sabemos que es una tupla por estar entre parentesis.
#print(type(x))

#y = tuple((1, 2, 3)) # si en una tupla no se ponen dobles parentesis en el ejecutor me salta error.
#print(y)

#print(x[0]) # en este caso es para saber la posicion de los elementos de la tupla.

x[1] = 10 # si hacemos esto me va a saltar error porque como dice anteriormente no se pueden reasignar los valores de la tupla.

del x # este termino ¨del¨ se usa para eliinar los valores de la tupla, entonces al ejecutar me va a saltar error porque ya no va a existir.
print(x)

# Tambien puedo usar las tuplas en los diccionarios 
location = {
    (39.000, 40.000): "Tokyo",
    (41.000, 29.000): "Japon"
}

print(location)