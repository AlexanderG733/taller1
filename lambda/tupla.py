
tuplas = [(2, "bmw"),(1, "chevrolet"),(2, "audi")]

ordenados = sorted(tuplas,key = lambda marca: marca[1])
print(ordenados)