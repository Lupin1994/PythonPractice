# Напишите программу, в которой пользователь будет задавать две строки, а программа 
# - определять количество вхождений одной строки в другой.
# Пример:
# Строка - "dabccabccabcc"
# Подстрока - "ab"
# Количество вхождений - 3
#***************************Первый способ*********************************************
# text = input('Write string: ')
text = str('dabccabccabcc')
f_text = input('Write search string: ')
count = 0
for i in range(0,len(text)-len(f_text)+1):
    if text[i:i+len(f_text)] == f_text:
        count+=1
print(count)
# ***************************Второй способ*********************************************

# string = str('dabccabccabcc')
# substring = input('Write search string - ')
# print(f'Count - {string.count(substring)}')