#В двумерном списке найти суммы элементов каждого столбца и поместить их в
#новый массив. Выполнить замену элементов второй строки исходной матрицы на
#полученные суммы.
import random

n = 3
m = 3

matrix = [[random.randint(-20,20) for i in range(n)] for i in range(m)]

print('n-мерный массив:')
for i in matrix:
    print(i)

sums = [sum(column) for column in zip(*matrix)]

matrix[1] = sums

print("\nновая матрица:")
for row in matrix:
    print(row)