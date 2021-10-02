a = int(input('введи а='))
b = int(input('введи b='))
c = int(input('введи c='))
if a < b + c and b < a + c and c < a + b:
    # print('построить треугольник возможно')
    if a == b == c:
        print('треугольник равносторонний')
    else:
        if a == b or b == c or c == a:
            print('треугольник равнобедренный')
        else:
            if a ** 2 == b ** 2 + c ** 2 or b ** 2 == a ** 2 + c ** 2 or c ** 2 == a ** 2 + b ** 2:
                print('треугольник прямоугольный')
            else:
                print('треугольник произвольный')
else:
    print("нет")
