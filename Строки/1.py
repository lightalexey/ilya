a = input('Введи число:')
k = len(a)
print('Количество разрядов', k)
print('крайняя правая цифра', a[k-1])
print('крайняя правая цифра', a[-1])
print('крайняя левая цифра', a[0])
summa = 0
for i in range(k):
    summa += int(a[i])

print('Сумма цифр равна', summa)