import random
cartas=[]
cant_cartas = int(input("Ingrese la cantidad de cartas:"))
for i in range(2):
    cartas.append([])
    for j in range(1, cant_cartas+1):
        cartas[i].append(j)
        random.shuffle(cartas[i])
print(cartas)
