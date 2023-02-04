# 28. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:

# 1) с помощью математических формул нахождения корней квадратного уравнения

# 2) с помощью дополнительных библиотек Python
#________________________________________________________________________
# A = int(input("Write A:"))
# B = int(input("Write B:"))
# C = int(input("Write C:"))
# dis = B**2 - 4*A*C
# if dis > 0:
#     x1 = ((-B) + dis**0.5)/2*A
#     x2 = ((-B) - dis**0.5)/2*A
#     print(f" x1 = {x1} , x2 = {x2}")
# elif dis == 0:
#     print(f"x = {-(B/2*A)}")
# else:
#     print("Корней нет")
#________________________________________________________________________
import math
A = int(input("Write A:"))
B = int(input("Write B:"))
C = int(input("Write C:"))

dis = math.pow(B,2) - 4*A*C
if A!=0:
    if dis > 0:
        # x1 = ((-B) + dis**0.5)/2*A
        # x2 = ((-B) - dis**0.5)/2*A
        x1 = (-B + math.sqrt(dis))/(2*A)
        x2 = (-B - math.sqrt(dis))/(2*A)
        print(f" x1 = {x1} , x2 = {x2}")
    elif dis == 0:
        print(f"x = {-(B/2*A)}")
    else:
        print("Корней нет")
else:
    print(f"x = {-C/B}")