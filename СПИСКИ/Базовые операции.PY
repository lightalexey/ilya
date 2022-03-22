from random import randrange
a = []
n = 10
print('Исходный список:')
for i in range(n):
    a.append(randrange(101)-50)
    print(a[i], end=' ')
print()
# решение начинается отсюда...
summa = 0
pr = 1
summpol = 0
kpol = 0
chet = 0
for i in range(n):
    summa += a[i]
    if a[i] != 0:
        pr *= a[i]
    if a[i] > 0:
        summpol += a[i]
        kpol += 1
    if a[i] % 2 == 0:
        chet += 1
print('Сумма всех элементов равна', summa)
print('Произведение всех ненулевых элементов равно', pr)
srar = summa / n
print(srar)
print(sum(a)/n)
print('Сумма положительных чисел', summpol)
print(kpol)
print(chet)
print('первый', a[0])
print('последний', a[n - 1])