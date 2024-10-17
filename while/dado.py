import random
numero6 = False
while not numero6:
    input("presiona enter para tirar el dado hasta que caiga el #6")
    numero = random.randint(1, 6)
    print("callo el numero: ",numero)
    if numero != 6:
        print("aun no cae 6")
    else:
        print("¡Callo el 6!")
        numero6 = True