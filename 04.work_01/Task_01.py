# 27. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел. 2 5 78 9
#________________________________________________________________________________________
# Str = (input("Write number with probel: ")).split(" ")
# max = int(Str[0])
# min = int(Str[0])
# for i in range(len(Str)):
#     if int(Str[i])>max:
#         max = int(Str[i])
#     if int(Str[i])<min:
#         min = int(Str[i])
# print(f"min = {min}, max = {max}")
#________________________________________________________________________________________
a = input()
list_num = a.split()
list_num = list(map(int,list_num))
print(max(list_num),min(list_num))