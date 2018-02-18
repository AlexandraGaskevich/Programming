import random

with open('slovar.csv', 'r', encoding = 'utf-8') as f:

    lines = f.readlines()

slvr = dict()

for line in lines:

    words = line.split(';')

    slvr[words[1]] = words[0]

    

keys = list(slvr.keys())

word1 = random.choice(keys)

a = len(word1) - 2



print('Угадайте второе слово')

print(slvr[word1], '...')

word2 = input()+'"' #я так и не смогла понять откуда тут берутся кавычки, программа их требует, и чтобы с ними не морочиться - я ввела их сама в ответ пользователя



if word2 == word1.strip():

    print('Верный ответ')

else:

    print('Ответ неверный, осталось 2 попытки')
    
    word2 = input()+'"'

    if word2 == word1.strip():
        print('Верный ответ')

    else:
        

        print('Ответ неверный. Нужна подсказка? (да или нет)')

        answer = input()

        if answer == 'да':
            print(a, 'букв')
        else:
            print('Осталась 1 попытка')
        
        word2 = input()+'"'
        
        if word2 == word1.strip():
            print('Верный ответ')

        else:
            print('Ответ неверный')
            print('Правильный ответ: "', word1)
        
