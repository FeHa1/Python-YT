# todas las funciones son las que estuvimos trabajando
#print()
#dir()
#type()

def hello(): # La sentencia ¨def¨ es una definición de función usada para crear objetos funciones definidas por el usuario
    print("hola")
hello() # se hace esto porque sino no lo reconoce, entonces tengo que "llamarlo" para que entienda que quiero imprimir en pantalla.


def hello(name): # esto lo uso para que pueda imprimir varios datos,al asignarle valores al ¨hello()¨ como son estos ejemplos, ya que concatenandiolos el ejecutor los reconoce.
    print("hola " + name)
hello("Fefe") 
hello("Ryan")


def add(Numberone, Numbertwo):
    return Numberone + Numbertwo # el termino ¨return¨ se usa para vpñver al codigo principal.
print(add(40, 50))



