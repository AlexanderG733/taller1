numero = int(input("Ingrese un numero: "))
suma = 0
while numero > 0:
    suma = suma + (numero % 10)
    numero = numero // 10
print(f"la suma de los digitos es: {suma}")