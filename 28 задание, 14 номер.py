symbol = '0123456789ABCDEF'
def ss(a, system):
    otvet = ''
    while a > 0:
        otvet = symbol[a % system] + otvet
        a //= system
    return otvet
print(ss(6*343**5+5*49**7-50,7).count('6'))