import csv
import re
import os

print ('Гаскевич Александра БКЛ172 Экзамен Задание 2')

def reading(filename):
    with open (filename, 'r') as f:
        text = f.readlines()
    return text

def abbr(t):
    d = {}
    for line in t:
        r = re.search('lex\="([А-Я]+[-]+[А-Я]+)', line) or re.search('lex\="([А-Я][А-Я]+)', line)
        
        
        if r:
            word = r.group(1)
            if word in d:
                d[word] += 1
            else:
                d[word] = 1
    
    print('Аббревиатура', 'Количество_вхождений')
    for word in sorted (d, key = d.get, reverse = True):
       print('{}\t{}'.format(word, d[word]))
#не разобралась, как посчитать количество вхождений одного слова во всех текстах сразу :(

    FILENAME2 = "information.csv"
    information = [
        [word, d[word]]
        ]
    with open(FILENAME2, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(information)
#это была попытка создать таблицу

def noun(t):
    d = {}
    for line in t:
        r = re.search('gr="S,m,[a-z]=sg,nom"', line)
        
        
        if r:
            word = r.group(1)
            if word in d:
                d[word] += 1
            else:
                d[word] = 1
    print('rrr')
    for word in sorted (d, key = d.get, reverse = True):
       print('{}\t{}'.format(word, d[word]))
    
def main():
    abbr(reading('_itartass1.xhtml'))
    abbr(reading('_itartass2.xhtml'))
    abbr(reading('_itartass3.xhtml'))
    abbr(reading('_itartass4.xhtml'))
    abbr(reading('_itartass5.xhtml'))
    abbr(reading('_rbk2.xhtml'))
    abbr(reading('_rbk3.xhtml'))
    abbr(reading('_rbk4.xhtml'))
    abbr(reading('_rbk6.xhtml'))
    abbr(reading('_rbk7.xhtml'))
    abbr(reading('_rian1.xhtml'))
    abbr(reading('_rian2.xhtml'))
    abbr(reading('_rian3.xhtml'))
    abbr(reading('_rian5.xhtml'))
    

if __name__ == "__main__":
    main()



