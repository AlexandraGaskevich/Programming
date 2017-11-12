word = list(input ("Введите слово: "))

a=len(word)
for i in range(a):
    print("".join(word[i:]))
