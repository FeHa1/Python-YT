#nombre simbolico para un valor (se expresa por el ¨=¨)
#el ¨name¨ es la palabra clave para el valor que estoy usando como ejemplo en este momento.
name = "Fazt"

print(10 + 101)

print(name)

x, book = 100, "I Robot"

print(x, book)

#se puede agregar cualquier palabra clave para un valor.
x = "200"

#case sensitive (se crea otra variable con distintos nombres aunque parezcan iguales, la mayuscula lo diferencia)
book = "21 lecciones para el siglo 21"
Book = "21 lecciones para el siglo 21"

#conventiones (formas en la que los programadores escriben sus variables)
#se colocan ¨_¨ para que sea mas leible para los programadores.
book_name = "I Robot" #Snake Case (cuando se separa por ¨_¨)
bookName = "TF2" #Camel Case (cuando la variable empieza en minuscula y la segunda palabra en mayuscula)
BookName = "ljljljljljljljl" #Pascal Case (caundo empieza con mayuscula y la segunda palabra tambien)

#constante (valor que nunca cambia)
PI = 3.1416 #cuando lo pongo en mayuscula se entiende, para otro programador, que nunca va a cambiar

#las variables pueden ser reasignadas, en este caso paso de letras a numeros, por eso se dice que Python es un lenguaje de tipado dinamico.
book_name = "I Robot"
book_name = 1234567890
