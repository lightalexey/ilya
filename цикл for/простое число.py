x = int(input('Введи число:'))
k = 0
for i in range(1, x + 1):
    if x % i == 0:
        k += 1
if k == 2:
    print('число простое')
else:
    print('число составное')
# 2 способ
k = 0
for i in range(2, x//2 + 1):
    if x % i == 0:
        k += 1
        break
if k == 0:
    print('число простое')
else:
    print('число составное')
# 3 способ
flag = True
for i in range(2, x//2 + 1):
    if x % i == 0:
        flag = False
        break
if flag:
    print('число простое')
else:
    print('число составное')