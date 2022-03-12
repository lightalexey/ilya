f = open('24_demo (1).txt')
s = f.read()
# print(len(s))
# Определите длину самой длинной последовательности, состоящей из символов X.
# Хотя бы один символ X находится в последовательности.
result = 1
tek = 1
for i in range(len(s)-1):
    # if s[i] == 'X' and s[i+1] == 'X':
    if s[i] == s[i + 1] == 'X':
        tek += 1
    else:
        if tek > result:
            result = tek
        tek = 1
print(max(result, tek))