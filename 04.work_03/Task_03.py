# 29. Задайте два числа. Напишите программу, 
# которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
#_________________________________________________________________
# a = int(input("Write a: "))
# b = int(input("Write b: "))
# for i in range(1,a*b):
#     if i%a == 0 and i%b ==0:
#         print(f"HOK = {i}")
#         break
#__________________________________________________________________________
a = int(input("Write a: "))
b = int(input("Write b: "))
for i in range(max(a,b),a*b+1,max(a,b)):
    if i%a == 0 and i%b ==0:
        print(f"HOK = {i}")
        break