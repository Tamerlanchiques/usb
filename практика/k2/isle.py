import os
import math
def win(word):
    print('')
    print('Было загадано слово ' + word + ' и вы его отгадали!')
print('Добро пожаловать в игру по спасению острова!')
word = input('Введите загадываемое слово: ')
wordLength = len(word)
hiddenWord = list()
guessedLetters = []
for i in range(wordLength):
    hiddenWord.append('*')
'''
Переменные, значение которых не меняется со временем, пишутся заглавными буквами.
Такие переменные называются константами.
'''
ISLE_HEALTH_MAX = math.ceil(wordLength / 2) 
isleHealth = ISLE_HEALTH_MAX
progress = 0
os.system('cls' if os.name == 'nt' else 'clear')
print('Загадано слово '+''.join(hiddenWord) +
      '. Начните отгадывать его по одной букве')
while not (progress == wordLength):
    letter = input('Введите букву или слово целиком: ')
    isAlreadyGuessed = False
    for a in range(len(guessedLetters)):
        if(guessedLetters[a] == letter):
            print('Буква '+letter+' уже была. Попробуйте другую.')
            isAlreadyGuessed = True
            break
    if not isAlreadyGuessed:   
        guessedLetters.append(letter)
    else:
        continue
    if(letter.lower() == word.lower()):
        win(word)
        break
    if(len(letter)>1):
        print('Разрешенно вводить или слово целиком, или одну букву. Не пытайся читерить!')
        continue
    letterIndexes = list()
    for i in range(wordLength):
        if(word[i] == letter):
            letterIndexes.append(i)
    letterIndexesLength = len(letterIndexes)
    if(letterIndexesLength != 0):
        progress += letterIndexesLength
        for i in range(letterIndexesLength):
            hiddenWord[letterIndexes[i]] = letter
        print('Буква '+letter+' есть в загаданном слове '+''.join(hiddenWord))
        if(progress == wordLength):
            win(word)
            break
        else:
            continue
    else:
        isleHealth -= 1
        if(isleHealth < 1):
            print('Вы не угадали и ваш остров ушёл под воду =( F')
            print('Было загадано слово ' + '\"'+word+'\"')
            break
        else:
            print('Такой буквы нет. Здоровье острова: ' +
                  str(isleHealth)+' / '+str(ISLE_HEALTH_MAX))
            continue