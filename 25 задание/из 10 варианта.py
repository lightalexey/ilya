for i in range(350000, 360000):
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            min = j
            break
    for j in range(i // 2, 1, -1):
        if i % j == 0:
            max = j
            break
    if (max - min) % 23 == 9:
        print(i, max - min)