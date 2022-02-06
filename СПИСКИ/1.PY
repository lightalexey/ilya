a = []  # a[0] a[1] ....
n = int(input('Введи количество элементов:'))
for i in range(n):
    new_element = int(input('Введи элемент:'))
    a.append(new_element)
print('Исходный список:')
for i in range(n):
    print(a[i], end=' ')
print()
print('еще раз:')
print(a)