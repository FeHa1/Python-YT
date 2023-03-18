x = 10
y = 20
w = 30
# cuando colocamos el print por debajo de lo que queremos comparar (presionando Tab lo separamos de toque) le estamos pidiendo que lo imprima solo si ¨x¨ es menor que 30
if x < 30: # se usa el termino ¨if¨ para comparar, y siempre hay que colocar los dos punto ¨:¨
    print("x is less than 30") # se va a mostrar en el ejecutor solo si es True que 30 es mallor que ¨x¨.

if y == 20: # se usa el termino ¨if¨ para comparar, y siempre hay que colocar los dos punto ¨:¨
    print("y is the same as 20") # se va a mostrar en el ejecutor solo si es True que 20 es lo mismo que  ¨y¨

if w > 40: # se usa el termino ¨if¨ para comparar, y siempre hay que colocar los dos punto ¨:¨
    print("w is more than 50")
else: # esto significa que si es el caso contrario al ¨if¨, en lugar de no mostrarlo en pantalla, solo lo va a reemplazar por otro valor asignado.
    print("w is less than 50")

# tambien se puede hacer con colores
colors = "red"
if colors == "blue":
    print("colors is blue")
# es el punto medio entre ¨if¨ y ¨else¨.
elif colors == "red": 
    print("the color is red")
else: 
    print("colors is not blue")

# tambien se pueden poner ¨if¨ dentro de otros ¨if¨
name = "John"
last_name = "Carter"
if name == "John":
    if last_name == "Carter":
        print("You are John Carter")
    else: 
        print("You are not John Carter")



