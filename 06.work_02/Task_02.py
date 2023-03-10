# 42)Напишите программу, которая сортирует отдельно элементы массива с чётными и нечётными значениями.
# Все элементы с нечётными значениями нужно отсортировать по возрастанию, 
# а элементы с чётными значениями – по убыванию. При этом элементы каждой из групп 
# (как чётные, так и нечётные) должны занимать то же множество позиций в массиве, что и до сортировки.

# Входные данные
# 6
# 3 1 2 5 4 6
# Первая строка содержит размер массива N . Во второй строке через пробел задаются N чисел – элементы массива. 
# Гарантируется, что 0 < N ≤ 100000 .

# Выходные данные
# 1 3 6 5 4 2
# Программа должна вывести все элементы отсортированного массива в одну строку, разделив их пробелами.
# lambda, filter

a = [3, 1, 2, 5, 4, 6]
print(a)
h = [1 if i%2==0 else 0 for i in a]
print(h)
even = [i for i in a if i%2==0]
odd = [i for i in a if i%2!=0]
even.sort(reverse= True)
odd.sort()

for index,value in enumerate(h):
    if value == 1:
        h[index] = even.pop(0) 
    else:
        h[index] = odd.pop(0)
        
print(h)