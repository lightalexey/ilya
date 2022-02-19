a = 1234653457
system = 3
otvet = ''
while a > 0:
    r = str(a % system)
    otvet = r + otvet
    a = a // system

print(otvet)
print(len(otvet))
print(otvet.count('0'))