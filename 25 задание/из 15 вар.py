for N in range(100000, 300000):
    if N % 7 == 0:
        for m in range(0, 29, 2):
            for n in range(1, 11, 2):
                if N == 2**m*7**n:
                    print(N)