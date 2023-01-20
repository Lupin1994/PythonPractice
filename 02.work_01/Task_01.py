# Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# Каждый член последовательности больше предыдущего в 3 раза, знаки у элементов чередуются.
# *Пример:*

# - Для N = 5: 1, -3, 9, -27, 81
# a = abs(int(input('Write number: ')))
# p = 1
# for i in range(1,a+1):
#     print(i,p)
#     p = p*(-3)
n = int(input())
symbol = 1
print(symbol, end=" ")
for i in range(n-1):
    symbol *= -3
    print(symbol, end=" ")
    
