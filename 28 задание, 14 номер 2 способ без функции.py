a = 6*343**5+5*49**7-50
k = 0
while a > 0:
    if a % 7 == 6:
        k += 1
    a //= 7
print(k)