# 19. Реализуйте алгоритм задания случайных чисел без 
# использования встроенного генератора псевдослучайных чисел.
# n вводит пользователь вывести рандомное число в диапазоне от 0 до n
#_____________________________________________________________________________________
# import datetime
# def random_int(num):
#     rand = datetime.datetime.now().microsecond/10*6
#     return int((num+1)*rand)
# print(random_int(int(input())))
#___________________________________________________________________________________    
import datetime

def random_int(num):
    rand = datetime.datetime.now().microsecond%num
    return rand+1
print(random_int(int(input())))
#_____________________________________________________________________________________   
# import datetime
# import time
# # def random_int(num):
# #     rand = datetime.datetime.now().microsecond%num
# #     return rand+1
# for i in range(10):
#     time.sleep(0.01) # Задержка по времени!!
#     print(datetime.datetime.now().microsecond)