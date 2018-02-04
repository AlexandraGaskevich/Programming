import re

def open_file():

   with open("Pride_and_Prejudice.txt", encoding='utf-8') as f:

        f = f.read()

        f = list(filter(None, re.split('\W', f)))

        return f

def pre_omni(f):

    freq_dict = {}

    for i in range(len(f)):

        if f[i][:4] == "omni":

            if f[i] in freq_dict:

                freq_dict[f[i]] += 1

            else:

                freq_dict[f[i]] = 1

    return freq_dict

def no_pre_omni(f):

    freq_dict2 = {}

    for i in range(len(f)):

        if f[i][:4] == "omni":

            a = f[i][4:]
            if a in freq_dict2:

                freq_dict2[a] += 1

            else:

                freq_dict2[a] = 1

    return freq_dict2

def word_with_omni(freq_dict):

    word_with_omni = []

    for word in freq_dict:

        if word[:4] == "omni": 

            word_with_omni.append(word)

    return word_with_omni

def word_amount(freq_dict):

    word_amount_list = sum(list(freq_dict.values()))

    return word_amount_list

def word_without_omni(freq_dict2):

    word_without_omni = []

    for word in freq_dict2:

        if word[:4] == "omni": 

            a = word[4:]

            word_without_omni.append(a)

    return word_without_omni

def word_amount2(freq_dict2):

    word_amount2_list = sum(list(freq_dict2.values()))

    return word_amount2_list


print("Слова с приставкой omni: " + str(word_with_omni(pre_omni(open_file()))))

print("Количество этих слов: " + str(word_amount(pre_omni(open_file()))))

print("Те же слова без приставки omni: " + str(word_without_omni(no_pre_omni(open_file()))))

print("Количество этих слов: " + str(word_amount2(no_pre_omni(open_file()))))


