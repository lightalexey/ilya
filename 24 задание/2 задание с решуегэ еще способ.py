# f = open('24_demo (1).txt')
# s = f.read()
# Определите длину самой длинной последовательности, состоящей из символов X.
# Хотя бы один символ X находится в последовательности.
# s = s.replace('Y', ' ')
# s = s.replace('Z', ' ')
# a = s.split()
# print(a)
print(len(max(open('24_demo (1).txt').read().replace('Y', ' ').replace('Z', ' ').split())))
