import random


userGuess=-1

print("Здравствуй, как тебя зовут?")

myName = input()

NumberToGuess=random.randint(1,100)

print(''+myName+' я хочу сыграть с тобой в одну игру. ')

while userGuess!=NumberToGuess:

    userGuess=int(input("Угадай число от 1 до 100 "))

    if userGuess > NumberToGuess:

        print("Число должно быть меньше!")

    elif userGuess < NumberToGuess:

         print("Число должно быть больше!")

    else:

             print('ты угадал,' +myName+ ', это число = ' + str(NumberToGuess))

             #Конец игры - выйти из цикла while

             break