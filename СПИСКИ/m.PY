from random import randrange
a = []
n = 10
print('Исходный список:')
for i in range(n):
    a.append(randrange(101)-50)
    print(a[i], end=' ')
print()
# решение начинается отсюда...
maximum = a[0]
minimum = a[0]
imax = imin = 0
for i in range(n):
    if a[i] > maximum:
        maximum = a[i]
        imax = i
    if a[i] < minimum:
        minimum = a[i]
        imin = i

print(maximum, imax)
print(minimum, imin)
print(max(a))
