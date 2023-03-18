myStr = "Hello World"

#print(dir(myStr)) 

#el termino ¨.upper¨ es para que el texto lo reconozca en mayuscula cuando lo ejecuto.
print(myStr.upper())
#el termino ¨.lower¨ es para que el texto lo ejecute en mayuscula cuando lo ejecuto.
print(myStr.lower())
#el termino¨.swapcase¨ es para que el texto lo ejecute al inverso (en este caso hELLO wORLD)
print(myStr.swapcase())
#el termino ¨.replace¨ sirve para reemplazar el texto original con otra palabra
print(myStr.replace("Hello", "Bye"))
#el termino ¨.count¨ sirve para contar letras/numeros/espacios que tiene el texto/String original.
print(myStr.count("W"))
#el termino ¨.startswith¨ sirve para identificar si la palabra con la que empieza el texto es la misma con
#la que empezamos, cuando lo ejecutemos nos lo va a representar como True o False (es la manera en la que el programa dicesi o no)
print(myStr.startswith("Hello"))
#el termino ¨.endswith¨ sirve para identificar si la palabra con la que termina el texto es la misma con la que termina el ejecutor.
print(myStr.endswith("World"))
#el termino ¨.split¨ sirve para separar los caracteres del texto original. Los separa por ¨,¨
print(myStr.split()) 
#el termino ¨.find¨ es para que encuentre la posicion de la letra con valor numerico, en este caso, 
#se cuenta desde la ¨H¨ como 0 y la ¨o¨ como 4.
print(myStr.find("o"))
#el termino ¨len¨ es para saber la cantidad de caracteres que tiene el texto original/String.
print(len(myStr))
#el termino ¨.index¨ se usa para conocer el lugar especifico de una letra en el texto original.
#se cuenta desde la ¨H¨ como 0 y la ¨e¨ como 1
print(myStr.index("e"))
#el termino ¨.isnumeric¨ se usa para saber si tiene algun numero dentro del String.
print(myStr.isnumeric())
#el termino ¨.isalpha¨ es para saber si el String es alfabetico y no tiene espacio entre sus caracteres.
print(myStr.isalpha())
#cuando ya sabemos la posicion de cada caracter podemos buscalo por valores numericos.
#en este caso la ¨o¨ esta en la posicion 4 por eso al ejecutarlo nos da una letra, y se coloca entre ¨[]¨
print(myStr[4])

