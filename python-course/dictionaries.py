# el diccionario se usa para definir datos de una manera mas completa

carrito = {
    "name": "book",
    "quantity": 3,
    "price": 4.99
}

print(carrito)

person = {
    "firts_name": "Ryan",
    "last_name": "Ray"
}

print(person.keys()) # el termino ¨.keys¨ se usa para obtener en pantalla solamente las llaves.
print(person.items()) # el termino ¨.items¨ se usa para obtener en pantalla los terminos con sus respectivos valores, y al ejecutarlo los pondra dentro de una tupla para diferenciarlos.

#del person # este termino es para eliminar los datos de la lista.
#print(person)

# tambien se pueden hacer listas de distintos diccionarios
diccionario = [
    {"amigos": "beisbolistas"},
    {"colegio": "tarea"},
]

print(diccionario)

