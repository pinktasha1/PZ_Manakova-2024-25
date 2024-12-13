#3. Дан список размера N. Осуществить сдвиг элементов список вправо на одну позицию
# (при этом A1 перейдет в A2, A2 — в A3, ..., AN-1 — в AN, a исходное значение последнего элемента будет потеряно).
# Первый элемент полученного списка положить равным 0.

import random

n = input('Сколько в списке будет символов? ')

while type(n) != int: #обработка исключений
  try:
    n = int(n)
  except ValueError :
    print('Неправильно ввели!')
    n = input('Введите число заново: ') #пусть пользователь введёт число заново

original_a = []

for i in range(n):
  original_a.append(random.randint(-100, 100))


def offset(original_a):
    result_a = [0] + original_a[:-1]
    return result_a


print('Твой список: ', original_a)
print('Твой изменённый список: ', offset(original_a))