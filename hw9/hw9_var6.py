import re

with open('text.txt', 'r', encoding='utf-8') as f:

        text = f.read()
        text = text.lower()
#print(text)
       
all_results = re.findall('загрузи', text)
all_results2 = re.findall('загрузи[вл]', text)
all_results3 = re.findall('загрузи[лт][аеиоь]', text)
all_results4 = re.findall('загрузи[в][ш][аеи][йея]', text)
a = all_results+all_results2+all_results3+all_results4

a1=list(set(a))

#программа выдает также формы которых в тексте нет, я пыталась убрать их:

b=text.split()
i=0
k=len(a1)

a2=[]
while i<k:
    if a1[i] in b:
        
        a2.append(a1[i])
    
    i+=1

print(a2)
