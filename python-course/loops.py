foods = ["apples", "milk", "bread", "cheese", "bananas"]

# print(foods[1]) 
# print(foods[2])
# print(foods[3])

# significa que en la lista de alimentos va a imprimir en el ejecutor cada uno de los alimentos sin necesidad de hacerlo por separado como en el ejemplo de arriba.
#for food in foods: # tambien se les puede agregar condicionales
    #if food == "milk":
        #print("you have to buy it")
    #else:
       # print("you do not have to buy it")
    #print(food) 


for food in foods:
    if food == "milk":
        break # cuando colocamos este ¨break¨ le estamos diciendo que cuando llegue a ¨milk¨ pare de imprimir el resto de la lista
    print(food)

for food in foods:
    if food == "milk":
        continue # cuando colocamos ¨continue¨ le estamos diciendo que cuando llegue a ¨milk¨ salte este dato de la lista y conntinue con el resto
    print(food)


