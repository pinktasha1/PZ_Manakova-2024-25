#В двумерном списке найти среднее арифметическое положительных элементов.
import random

n = 3
m = 2 #размеры списка

matrix = [[random.randint(-20,20) for i in range(n)] for i in range(m)]

print('двумерный массив:')
for i in matrix:
    print(i)

positive_num =  [num for n in matrix for num in n if num > 0]

print('среднее арифметическое положительных элементов:', sum(positive_num)/len(positive_num))