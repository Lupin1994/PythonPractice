# 20. Задайте список. Напишите программу, которая определит, 
# присутствует ли в заданном списке строк некое число.
#_______________________________________________________________
# list = ['re','2','er','45','6','1','jfd','w4f','2']
# list_new = None
# count = 0
# for i in range(len(list)):
#     list_new = list[i]
#     print(list_new,end = " ")
#     if list_new.isdigit():
#         count+=1
# print()
# print(f'Колличество цифр в списке = {count}')
#_______________________________________________________________       

a = ["sr","ere",12,"wewe"]
n = int(input())
if n in a:
    print(a.index(n))
else:
    print(-1)