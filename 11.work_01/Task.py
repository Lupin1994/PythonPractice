import math
from sympy import*
from sympy.plotting import plot
from numpy import*
# 
# Задача 1 
# Дана функция F(x) = 5x^2 + 10x -30
# 1) Определить корни

# 2)Найти интервалы, на которых функция возрастает

# 3)Найти интервалы, на которых функция убывает

# 4)Построить график

# 5)Вычислить вершину

# 6)Определить промежутки, на котором f > 0

# 7)Определить промежутки, на котором f < 0

x = symbols('x')
fx = 5*x**2 + 10*x -30
# Корни
print(solve(fx))
korn1, korn2 = solve(fx)
print(korn1, korn2)
# Найти интервалы,на которых функция возрастает
# y = diff(fx)
# print(solve(y>0))
# Построить график
solve(plot(fx))
# Вычислить вершину
print(solve(y))
# 6)Определить промежутки, на котором f > 0
print(solve(fx>0))
# 7)Определить промежутки, на котором f < 0
print(solve(fx<0))