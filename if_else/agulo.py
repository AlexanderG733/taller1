angulo = float(input("Escriba un angulo: "))

if angulo >= 0 and angulo <= 90:
    print("El angulo se encuentra en el primer cuadrante")
elif angulo >=91 and angulo <= 180:
    print("El angulo se encuentra en el segundo cuadrante")
elif angulo >180 and angulo < 270:
    print("El angulo se encuentra en el tercer cuadrante")
elif angulo >= 270 and angulo <= 360:
    print("El angulo se encuentra en el cuarto cuadrante")