print('Вариант 6. Программа должна получить от пользователя подряд 7 чисел, а после этого записать в файл 7 строчек, состоящих из соответствующего числа букв X (на первой строчке количество иксов равно первому введённому числу, на второй -- второму и т.д.')

a = []
for i in range(7):
    a.append(int(input('Введите число:')))
i=0
while i<7:
    b=a[i]
    if b > 0:
       print('X'*b)
    else:
        print('Число отрицательное.')
    i+=1

