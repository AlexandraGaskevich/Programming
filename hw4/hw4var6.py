with open("text.txt") as f:
   text = f.read()   
   splited_text = text.split()    
print (splited_text)
 

a=len(splited_text)
print("Количество слов в тексте: ", a)
i=0
for w in splited_text:
        if w[0].isupper():
            i+=1;
        else: i+=0
print("Количество слов с заглавной буквой в тексте: ",i)
percent=int(i/a*100)
print("Процент слов, начинающихся с заглавной буквы: ",percent, "%")
