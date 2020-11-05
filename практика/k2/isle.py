import os
print('Добро пожаловать в игру по спасению острова!')
word = input('Введите загадываемое слово: ')
wordLength = len(word)
hiddenWord = list()
for i in range(wordLength):
    hiddenWord.append('*')
isleHealthMax = 4
isleHealth = isleHealthMax
progress = 0
os.system('clear')
print('Загадано слово '+''.join(hiddenWord) +
      '. Начните отгадывать его по одной букве')
while not (progress == wordLength):
    letter = input('Введите букву или слово целиком: ')
    if(letter.lower()==word.lower()):
        progress = wordLength
        break
    letterIndexes = list()
    for i in range(wordLength):
        if(word[i])==letter:
            letterIndexes.append(i)
    letterIndexesLength = len(letterIndexes)
    if(letterIndexesLength != 0):
        progress += letterIndexesLength
        for i in range(letterIndexesLength):
            hiddenWord[letterIndexes[i]] = letter
        print('Буква '+letter+' есть в слове в загаданном слове '+''.join(hiddenWord))
        continue
    else:
        isleHealth -= 1
        if(isleHealth < 1):
            print('')
            print('Вы не угадали и ваш остров ушёл под воду =( F')
            print('Было загадано слово ' + '\"'+word+'\"')
            break
        else:
            print('Такой буквы нет =(. Здоровье острова: ' +
                  str(isleHealth)+' / '+str(isleHealthMax))
            continue
if(progress==wordLength):
    print('')
    print('Было загадано слово ' + word + ' и вы его отгадали!')

