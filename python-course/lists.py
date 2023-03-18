# List (su trabajo es agrupar datos ya sean diferentes o iguales, que se marcan con los ¨[]¨.) 
# (Y para decirle que son diferentes datos los separo por ¨,¨)
demo_list = [1, "hello", 1.34, True, [1, 2, 3]] # se pueden colocar listas dentro de otras listas. 
colors = ["red", "green", "blue"]

# Constructor (funcion que nos permite definir una lista)
#number_list = list((1, 2, 3, 4)) # le pongo los doble ¨()¨ porque la lista no reconoce mas de un dato en una lista, pero si le coloco dentro de una tupla lo reconoce como uno.
#print(type(number_list))

# El termino ¨range()¨ se usa para colocar de donde hasta donde quiero colocar determinado elemento.
#r = list(range(1, 10)) # cuando lo ejecute va a llegar hasta un numero antes del segundotermino (en este caso del 1 al 9)
#print(r) 

#print(dir(colors)) # el termino ¨dir¨ mostraba infomacion.
#print(len(colors)) # el termino ¨len¨ es para saber cuantos elementos tengo (en este caso son 3)
#print(len(demo_list)) 
#print(colors[1]) # el nombre de la variable mas los ¨[]¨ se usan para saber la posicion en la que se encuentran las palabras al ejecutar.
#print("green" in colors) # el termino ¨in¨ es para saber si esta en la capeta de, en estecaso, colors. Y el ejecutor me dira True/False.
colors[1] = "yellow" # se marca la posicion en la carpeta del termino que queremos cambiar. El ejecutor lo va a mostrar cambiado.
#print(colors)
#print(dir(colors))
#colors.append("violet") # el termino ¨.append¨ es para agregar un nuevo elemento a la lista.
print(colors)
#colors.append("violet", "yellow") # esto daria eror porque no puedo colocar dos elementos en ¨.append¨
#colors.append(("violet", "yellow")) # asi si se puede porque estan dentro de una tupla ¨(())¨
print(colors)
#colors.extend(("violet", "yellow")) # el termino ¨.extend¨ sirve para extender la lista y que me los tome como terminos independientes al ejecturalo, pero solo si lo coloco dentro de una tupla.
print(colors)
#colors.insert(1, "purple") # el termino ¨.inset¨ es para agregar terminos a la lista sin reemplazar los ya presentes, solo los agrega en la posicion pedida.
print(colors)
#colors.pop(1) # el termino ¨.pop¨ se usa para eliminar elementos de las listas, pero va quitando a partir de lasposiciones numericas.
print(colors) 
#colors.remove("red") # este termino ¨.remove¨ sí se usa para remover elementos especificos de una lista.
print(colors)
#colors.clear() # el termino ¨.clear¨ es para limpiar todos los lementosde la lista. 
print(colors)
#colors.sort() # este termino ¨.sort¨ se usa para ordenar los elementos alfabeticamente  
print(colors)
#colors.sort(reverse=True) # guiados por el mismo termino de ¨.sort¨ le pedimos al ejecutor que nos lo ordene alfabeticamente al inversode como es en realidad.
print(colors)
#print(colors.index("red")) # el termino ¨.index¨ se utiliza para saber la posicion numerica de los terminos al ejecutar.
print(colors.count("blue")) # el termino ¨.count¨ es para contar la cantidad de veces que se repite el termino, en este caso blue, en la lista. 
