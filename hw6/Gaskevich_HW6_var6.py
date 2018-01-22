import random

def noun():

    nouns = ['neko', 'inu', 'tomodachi', 'onna no ko', 'mori', 'hon']

    return random.choice(nouns)





#def adverb():

    # эта функция возвращает случайное наречие; у неё нет аргументов

    #nouns = ['aggressively', 'loudly', 'slowly', 'proudly', 'dangerously']

    #return random.choice(nouns)





#def intensifier(adv):

    # эта функция добавляет к наречию adv наречие-модификатор

    # и возвращает результат

    #intensifiers = ['quite', 'rather', 'very', 'enough']

    #random_intensifier = random.choice(intensifiers)

    #if random_intensifier == 'enough':

        #result = adv + ' ' + random_intensifier

    #else:

        #result = random_intensifier + ' ' + adv

    #return result





def adjective(word):

    adjectives = ['ookii', 'chiisai', 'atarashii', 'aoi', 'omoi', 'tsuyoi', 'omoshiroi', 'ii', 'kawaii']

    return random.choice(adjectives) + ' ' + word





def verb_of_thought(subj):

    verbs = ['kuretta', 'tomarimashita', 'deshita', 'mashita', 'sinaseru']

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





# А вот тут начинается основной код. Из одной строчки. :)

# Он распечатывает случайное предложение.

#print(random_sentence())

#print()



print("---- Текст, лишенный смысла ----")

for i in range(5):  # используем это число в цикле, чтобы несколько раз запустить генератор предложений

    sentence = random_sentence() # генерируем предложение

    sentence = sentence.capitalize() # capitalize() делает первую букву строки заглавной

    print(sentence, end=' ') 

print("\n--------- Примечание: Простите, я пока плохо знаю правила японского языка, чтобы писать условные и побудительные предложения, так что моя программа выдает только три вида японских предложений. ---------")
