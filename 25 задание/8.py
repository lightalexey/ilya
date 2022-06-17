for i in range(95632, 95650+1):
    k = 0
    for j in range(1, i+1):
        if i % j == 0 and j % 2 != 0:
             k += 1
    if k == 6:
       # print(i)
       for j in range(1, i+1, 2):
           if i % j == 0:
               print(j, end=' ')
       print()

# # улучшить
# print('2 способ')
# for i in range(956320, 956500+1):
#     k = 0
#     for j in range(3, i//2+1, 2):
#         if i % j == 0:
#              k += 1
#     if k == 4:
#         print(i)