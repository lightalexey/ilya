s = int(input('Введите строку:'))
count = 0
for i in range(s):
    if s == 'a' or s == 'e' or s == 'i' or s == 'o' or s == 'u':
        count += 1
print('Количество гласных равно:', count)