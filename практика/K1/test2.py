import random
n = 0
mas = []  # массив целых чисел для отгадывания
for i in range(50):
    randomNumber = random.randint(0, 100)
    mas.append(randomNumber)

print(mas)
