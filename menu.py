import os
import random

os.system('cls')

def triangulo ():
   for i in range(1,+6+1):
    print(" "*(6-i)+" *"*(i-1))
    print("")
   menu1()

def letraAlfabeto():
    letra = str(input("escriiba una letra: "))
    if letra in "abcdefghijklmn":
        print(f"la letra, {letra}, esta en la primera mitad del alfabeto")
    else:
        print(f"la letra, {letra}, esta en la segunda mitad del alfabeto")
    print("")
    menu1()
def mayorDiez():
    numeros = [1,2,11,20,30,5,12,8]
    mayorDiez = list(filter(lambda num: num > 10 , numeros))
    print("lista de numeros mayores a 10 ",mayorDiez)
    print("")
    menu1()
def dado():
    numero6 = False
    while not numero6:
        input("presiona enter para tirar el dado hasta que caiga el #6 ")
        numero = random.randint(1, 6)
        print("callo el numero: ",numero)
        if numero != 6:
            print("aun no cae 6")
        else:
            print("¡Callo el 6!")
            numero6 = True
    print("")
    menu1()
def menu1():
    print("MENU EJERCICIOS")
    print("1. Triangulo con asteriscos")
    print("2. Indica si una letra es de las primeras del abecedario o de las ultimas")
    print("3. Los numeros mayores a 10 de una lista de numeros")
    print("4. Arroja un dado hasta que caiga el numero 6")
    print("5. SALIR")

    opcion = int(input("Seleccione el ejercicio que desee ver: "))
    if(opcion == 1):
        triangulo()
    elif(opcion == 2):
            letraAlfabeto()
    elif(opcion == 3):
            mayorDiez()
    elif(opcion == 4):
            dado()
    elif(opcion == 5):
         print("¡GRACIAS!")
    else:
         print("")
         print("SELECCIONE UNA OPCION VALIDA")
         print("")
         menu1()
menu1()