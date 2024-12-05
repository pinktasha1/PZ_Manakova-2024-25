#2. Описать функцию Minmax(X, Y), записывающую в переменную X минимальное из значений X и Y,
# а в переменную Y — максимальное из этих значений (X и Y — вещественные параметры,
# являющиеся одновременно входными и выходными).
# Используя четыре вызова этой функции, найти минимальное и максимальное из данных чисел A, B, C, D.
from typing import final


def min_max(x, y): #x - минимальное значение, y - максимальное значение
    if x > y:
        x , y = y , x #меняю порядок значений если x > y
    return x, y


def exception(var, message): #обработка исключений
  while type(var) != float:
    try:
      var = float(var)
    except ValueError:
      print('Неправильно ввели!')
      var = input(message)
  return var


a = input('Введи число a: ')
a = exception(a, "Введи число заново")

b = input('Введи число b: ')
b = exception(b, "Введи число заново")

c = input('Введи число b: ')
c = exception(c, "Введи число заново")

d = input('Введи число b: ')
d = exception(d, "Введи число заново")

#нахожу пары минимальных и максимальных значений
min_ab, max_ab = min_max(a, b)
min_cd, max_cd = min_max(c, d)
#нахожу минимум и максимум из пар
final_min, _ = min_max(min_ab, min_cd)
_, final_max = min_max(max_cd, max_ab)

print(f'Минимальное число: {final_min}\nМаксимальное число: {final_max}')
