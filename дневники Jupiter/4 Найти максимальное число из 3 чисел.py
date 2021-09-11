a = int(input('введи а='))
b = int(input('введи b='))
c = int(input('введи c='))
if a > b and a > c:
    print(a)
if b > a and b > c:
    print(b)
if c > a and c > b:
    print(c)

print(max(a, b, c))


