# Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.

# *Примеры:*

# - 6,78 -> 7
# - 5 -> нет
# - 0,34 -> 3
# a = float(input('a = '))
# print(int(a*10%10))
n = input()
list_num = n.split(",")
if len(list_num)>1:
    print(list_num[1][0])