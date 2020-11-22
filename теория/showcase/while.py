people = ['Вася', 'Петя', 'Боря', 'Маша', 'Диана', 'Валерия', 'Даниил']
i = 0
search = input('Введите имя: ')
current = ''
while not current == search or i == len(people):
    current = people[i]
    print(current)
    
    if(current == search):
        print('Стажёр ' + search + ' найден, его порядковый номер '+str(i))
        break
    if i<len(people)-1: 
        i += 1
    else:
        break
if current != search:
    print('Стажёра по имени '+search+' не найдено')

    