# перевод до 16СС
symbol = '0123456789ABCDEF'
def ss(a, system):
    otvet = ''
    while a > 0:
        otvet = symbol[a % system] + otvet
        a //= system
    return otvet

print(ss(12**13,13))
