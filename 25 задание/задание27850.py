n = 0
for a in range(245690, 245756+1):
    k = 0
    n += 1
    for i in range(2, a // 2 + 1):
        if a % i == 0:
            k += 1
    if k == 0:
        print(n, a)