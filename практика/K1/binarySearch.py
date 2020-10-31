import random
# двоичный поиск
# https://codelessons.ru/cplusplus/algoritmy/binarnyj-poisk-po-massivu-c.html
# .sort()
# сначала сделать просто поэлементный поиск, показать несовершнество исходя из количества итераций поиска
# показываем пример на отсортированных  неслучайных числах
# меняем на рандом
mas = list(range(100000))
""" mas = []  # массив целых чисел для отгадывания
for i in range(100): # в нашем массиве будет 50 случаных чисел
    randomNumber = random.randint(0, 100) # получаем от библиотеки random случайное число от 0 до 100 и …
    mas.append(randomNumber) # … добавляем это число в наш массив
mas.sort() """
# создали переменную в которой будет находиться ключ
key = int(input('Введите число для поиска: '))

success = False
iterateCounter = 0 # счётчик повторений цикла поиска
l = 0  # левая граница
r = mas[len(mas)-1]  # правая граница
mid = None

while ((l <= r)):
    iterateCounter+=1
    mid = (l + r) // 2  # считываем срединный индекс отрезка [l,r]
    if (mas[mid] == key):
        success = True  # проверяем ключ со серединным элементом
    if (mas[mid] > key):
        r = mid - 1  # проверяем, какую часть нужно отбросить
    else:
        l = mid + 1


if (success==True):
    print("Индекс элемента " + str(key) + " в массиве равен: " + str(mid))
    print("")
    print("Количество циклов поиска искомого числа: "+str(iterateCounter))
else:
    print("Извините, но такого элемента в массиве нет")
