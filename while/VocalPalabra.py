
vocales = "aeiouAEIOU"
i = 0
contVocales = 0
palabra = input("Escribe una palabra: ")

while i < len(palabra):
    if palabra[i] in vocales:
        contVocales += 1
    i += 1
print(f'La cantidad de vocales en la palabra {palabra} son: {contVocales}')