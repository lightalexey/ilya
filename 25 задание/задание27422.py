for a in range(174457, 174505+1):
    k = 0
    for i in range(2, a // 2 + 1):
        if a % i == 0:
            k += 1
            if k > 2:
                break
    if k == 2:
        # print(a)
        for j in range(2, a//2 + 1):
            if a % j == 0:
                print(j, end=' ')
        print()
