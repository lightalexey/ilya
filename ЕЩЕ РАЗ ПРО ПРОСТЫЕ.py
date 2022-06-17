a = 100000000
b = 100000500
for x in range(a, b + 1):
    k = 0
    for i in range(2, int(x ** 0.5) // 2 + 1):
        if x % i == 0:
            k += 1
            break
    if k == 0:
        print(x, end=' ')

