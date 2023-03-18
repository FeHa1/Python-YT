# es una coleccion desordenada sin indice, se usan para definir una coleccion sin indice 
colors = {"Red", "Green", "Blue"}
#print(type(colors)) # nos va a decir el ejecutor que es tipo ¨set¨

#print("Red" in colors) # esto termino ¨in¨ es para saber si "Red" esta en la carpeta de colors

colors.add("Violet") # este ¨.add¨ es para que agregue elementos a la lista, pero al ejecutarlo, como no tienen indice, me lo va a poner donde quiera el interprete.
#print(colors)

colors.remove("Green") # este termino ¨.remove¨ es para remover datos de la coleccion.
#print(colors)

colors.clear() # el terrmino ¨.clear¨ se usa para limpiar todos los elementos de la coleccion
print(colors) 

