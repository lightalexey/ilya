# 1 способ
symbol = '0123456'
def ss(a, system):
    otvet = ''
    while a > 0:
        otvet += symbol[a % system]
        a //= system
    return otvet
# print(ss(103*7**103-5*7**57+98, 7))
s = ss(103*7**103-5*7**57+98, 7)
summa = 0
for i in range(len(s)):
    summa += int(s[i])
print(summa)
# 2 способ
s = 103*7**103-5*7**57+98
chislo = ''
while s > 0:
    number = str(s % 7)
    chislo =  chislo + number
    s //= 7
#print(chislo)
summa = 0
for i in range(len(chislo)):
    summa += int(chislo[i])
print(summa)
# 3 способ
summa = 0
s = 103*7**103-5*7**57+98
while s > 0:
    summa += s % 7
    s //= 7
print(summa)