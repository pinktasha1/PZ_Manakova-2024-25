# В двумерном списке элементы третьей строки заменить элементами из одномерного
#динамического массива соответствующей размерности.
import random

n = 5
m = 5 #размеры списка

matrix = [[random.randint(-20,20) for i in range(n)] for i in range(m)]

print('n-мерный массив:')
for i in matrix:
    print(i)

new_matrix = [random.randint(-20,20) for i in range(n)]

print('\nодномерный массив: ',new_matrix)

matrix[2].clear()
matrix[2].extend(new_matrix)

print('\nновый массив:')
for i in matrix:
    print(i)