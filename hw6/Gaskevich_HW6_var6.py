import random

def noun():
    with open('Gaskevich_HW6_nouns.txt', 'r', encoding='utf-8') as f:
        nn = f.read()
        nouns = nn.split(', ')

        return random.choice(nouns)






def adjective(word):
    with open('Gaskevich_HW6_adjectives.txt', 'r', encoding='utf-8') as j:
        aa = j.read()
        adjectives = aa.split(', ')
        
        return random.choice(adjectives) + ' ' + word





def verb_of_thought(subj):

    with open('Gaskevich_HW6_verbs.txt', 'r', encoding='utf-8') as k:
        vv = k.read()
        verbs = vv.split(', ')

        return subj + ' ' + random.choice(verbs)





def punctuation():

    punctuations = ['.', 'ka?', 'ne!']

    return random.choice(punctuations)




def random_sentence():

    sentence = verb_of_thought(adjective(noun())+\
               ' ga ' + adjective(noun()) +\
               ' ni ' )+\
            ' '  + punctuation()

    return sentence


print("---- Текст, лишенный смысла ----")

for i in range(5): 

    sentence = random_sentence()

    sentence = sentence.capitalize()

    print(sentence, end=' ') 

print("\n--------- Примечание: Простите, я пока плохо знаю правила японского языка, чтобы писать условные и побудительные предложения, так что моя программа выдает только три вида японских предложений. ---------")
