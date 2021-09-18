a = int(input('введи а='))
b = int(input('введи b='))
c = int(input('введи c='))
if a < b + c and b < a + c and c < a + b:
    print('построить треугольник возможно')
else:
    print('построить треугольник невозможно')

# 2 способ - без использования and
if a < b + c:
    if b < a + c:
        if c < a + b:
            print('да')
        else:
            print('нет')
    else:
        print('нет')
else:
    print('нет')