# Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.
a = int(input('a = '))
if (a%5==0 and a%10==0 or a%15==0) and a%30!=0:
    print('Кратно')
else:
    print('Не кратно')
