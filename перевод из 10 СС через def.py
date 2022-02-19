# перевод до 16СС
def ss(a, system):
    otvet = ''
    while a > 0:
        r = str(a % system) # r = 0, 1, ... 15
        if r == '10':
            r = 'A'
        if r == '11':
            r = 'B'
        if r == '12':
            r = 'C'
        if r == '13':
            r = 'D'
        if r == '14':
            r = 'E'
        if r == '15':
            r = 'F'
        otvet = r + otvet
        a //= system
    return otvet

print(ss(9**18+3**54-9,3).count('2'))
