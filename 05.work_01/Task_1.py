from itertools import product
# Напишите программу на Python для поиска пересечения двух заданных массивов с помощью Lambda.
# [1, 2, 3, 5, 7, 8, 9, 10]
# [1, 2, 4, 8, 9]
b = [1, 2, 3, 5, 7, 8, 9, 10]
a = [1, 2, 4, 8, 9]
c = list(filter(lambda x: x in a ,b))
print(c)
#______________________________________________________
# c = [i for i,j in product(a,b) if i == j]
# print(c)
# #________________________________________________________
# for i,j in product(a,b):
#     if i == j:
#         c.append(i)
# print(c)
#____________________________________________________________
# for j in b:
#     for k in a:
#         if k == j:
#             c.append(j)
# print(c)
#____________________________________________________________
    