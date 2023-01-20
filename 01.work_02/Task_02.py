#1. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

# *Примеры:*

# - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

# a = abs(int(input('a = '))) abs- число по модулю

# for i in range(-a,a+1):
#     print(i, end = ",")

# a = abs(int(input('a = ')))
# print(list(range(-a,a+1)))

def func(N):
    if N>0:
        for i in range(-N,N+1):
            print(i, end=" ")
    else:
        for i in range(N,-N+1):
            print(i,end=" ")
N = int(input('Write number: '))
func(N)