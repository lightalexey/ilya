for i in range(100000):
    s = i
    n = 121
    while s < 124:
        s += 10
        n += 17
    if n == 291:
        print(i)