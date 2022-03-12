f = open('24_demo.txt')
s = f.read()
# print(len(s))
# Определите максимальное количество идущих подряд символов,
# среди которых каждые два соседних различны.
result = 1
tek = 1
for i in range(len(s)-1):
    if s[i] != s[i+1]:  # Цепочка растёт...
        tek += 1
    else: # Цепочка оборвалась
        if tek > result:
            result = tek
        tek = 1

# if tek > result:
#    result = tek

print(max(result, tek))