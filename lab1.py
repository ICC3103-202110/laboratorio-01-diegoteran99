import random

def crear_tablero(cant_cartas):
    tablero=[]
    for i in range(2):
        tablero.append([])
        for j in range(1,cant_cartas+1):
            tablero[i].append("▓")
    print(tablero)


cartas=[]
cant_cartas = int(input("Ingrese la cantidad de cartas:"))
for i in range(2):
    cartas.append([])
    for j in range(1, cant_cartas+1):
        cartas[i].append(j)
        random.shuffle(cartas[i])
print(cartas)

crear_tablero(cant_cartas)