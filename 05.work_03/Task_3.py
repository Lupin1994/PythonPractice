#37)Имеется упорядоченный список:
# A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Перебрать все элементы этого списка с помощью функций enumerate и элементы, 
# стоящие на главной диагонали (имеющие равные индексы), превратить в нули.

A = [[1, 2, 3], 
     [4, 5, 6], 
     [7, 8, 9]]

for index, value in enumerate(A):
    value[index] = 0
print(A)

for indx,val in enumerate(A):
    for indx2,val2 in enumerate(val):
        if indx == indx2:
            val[indx2] = 0
print(A)