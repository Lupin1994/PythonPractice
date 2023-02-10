# 36)Сделать с помощью filter, lambda
# Напишите программу, удаляющую из текста все слова, содержащие "абв".

# Вывести все пробелы и их индексы из предыдущей строки.

text = 'абв фвфывап абвцувф вбафак йцуауклд укйлт'

lst = text.split()
text2 = ' '.join(list(filter(lambda x: False if "абв" in x.lower() else True, lst)))
print(text2)
for i,sym in enumerate(text):
    if sym == ' ':
        print(f' индекс {i}, пробел {sym}')