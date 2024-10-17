tableroJedrez = [
    ["torreB", "caballoB", "alfilB", "reinaB", "reyB", "alfilB", "caballoB", "torreB"],
    ["peonB", "peonB", "peonB", "peonB", "peonB", "peonB", "peonB", "peonB"],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    ["peonN", "peonN", "peonN", "peonN", "peonN", "peonN", "peonN", "peonN"],
    ["torreN", "caballoN", "alfilN", "reinaN", "reyN", "alfilN", "caballoN", "torreN"]
]

def imprimir_tablero(tableroJedrez):
    for fila in tableroJedrez:
        print(" ".join(fila))
imprimir_tablero(tableroJedrez)
