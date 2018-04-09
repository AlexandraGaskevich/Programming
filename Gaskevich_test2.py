import re

print("Гаскевич Александра БКЛ172 Контрольная работа 2 вариант 2")

with open("f.xml","r",encoding="utf-8") as f:
    a = f.readlines()

b = len(a)
print("Количество строк: ", b)

with open("text.txt","w",encoding="utf-8") as file:

    file.write("Количество строк: ")
    file.write(str(b))

dict = {}
for line in a:
    
    if line.startswith('            <w lemma='):
        
        d = line.split('>')
        #print(d[1])
        
        words = {d[1]: "_"}
        dict.update(words)
        #print(dict)

with open("text.txt","w",encoding="utf-8") as file:

    file.write(str(dict))
