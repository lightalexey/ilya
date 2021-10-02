# квадратное уравнение вида ax2+bx+с=0
a = int(input())
b = int(input())
c = int(input())
D = b**2-4*a*c
if D < 0:
    print('нет действительных корней')
elif D > 0:
        x1 = (-b + D ** 0.5) / 2 / a
        x2 = (-b - D ** 0.5) / 2 / a
        print('x1=', x1)
        print('x2=', x2)
else:
        x1 = (-b + D ** 0.5) / 2 / a
        print('x1=x2=', x1)



