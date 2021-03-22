import random
cant_cartas = int(input("Ingrese la cantidad de cartas:"))
cartas = 2*list(range(1, cant_cartas+1))
random.shuffle(cartas)
print(cartas)