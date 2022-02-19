a = int(input('введи число = '))
system = int(input('введи систему счисления = '))
otvet = ''
while a > 0:
    r = str(a % system)
    otvet = r + otvet
    a = a // system

print(otvet)
