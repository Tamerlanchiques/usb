print('')
print('Добро пожаловать в мой мир, сдесь мы с тобой сыграем в игру "угадай число".Ты загадываешь число, а я его угадываю')
print('Введите случайное число. Если оно задано в массиве, то вы угадали')
print('')

mas = [3, 5, 67, -65, 34, 21]  # массив целых чисел для отгадывания
 # Присваиваем переменной значение, которое мы введём с клавиатуры.
 # Обращаем внимание, что мы преобразуем строку в целочисленный тип int
 # Если написать просто input() без int(), то интерпретатор не воспримет 
 # введёное значение как число и выдаст ошибку

point = int(input('Введите число и нажмите Enter: '))



print('')


length = len(mas)  # команда, вычисляющая размер массива под названием mas


 # Цикл, который переберёт все значения от 0 до числа, равного длине массива -1
 # Обратите внимание, что исчисление элементов массива начинается с 0!

for i in range(0,length):
    # Оператор if (ЕСЛИ) условие истинно, тогда выполнить код ниже
    if mas[i] == point:
        print("В ячейке массива номер " + str(i) + " записано число " +
              str(mas[i])+" == " + str(point)+" УСПЕХ")
        break  # остановить выполнение цикла, не дожидаясь конца, так как мы уже нашли соответствие
    else:  # оператор else (ИНАЧЕ) выполнить код ниже
        print("В ячейке массива номер " + str(i) + " записано число " +
              str(mas[i])+" != " + str(point))


print('')
print('СПРАВКА')
print("Два символа 'равно' == означают то, что два сравниваемых значения равны")
print("Сочетание символа восклицательного знака и равно != означент то, что два сравниваемых значения НЕ равны")

