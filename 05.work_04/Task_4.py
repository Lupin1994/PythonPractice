# 38)Имеется список id сотрудников из 10 элементов, каждый id - случайное число от 1 до 100
# Имеется список имен сотрудников из 10 элементов
# Сопоставьте каждому имени сотрудника его id, и выведите получившийся список.
# Выведете имена сотрудников, получившие нечетное id. Решить с помощью zip,filter,lambda
from random import randint as rnd
id = [rnd(1,101) for _ in range(10)] # Элемент i не нужен по этому можно поставить _
names = ['Иванов',"Петров","Сидоров","Потапов","Михалков","Черемухов","Петухов","Гандонов","Дроздов","Лошков"]
lst = list(zip(id,names))
print(lst)
# lst_new = [elem[1] for elem in lst if elem[0]%2 !=0]
# print(lst_new)
lst_new = list(filter(lambda x: x[0]%2==1 ,lst))
print(lst_new)