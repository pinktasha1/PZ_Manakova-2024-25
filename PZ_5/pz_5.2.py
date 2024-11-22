#2. Описать функцию Minmax(X, Y), записывающую в переменную X минимальное из значений X и Y,
# а в переменную Y — максимальное из этих значений (X и Y — вещественные параметры,
# являющиеся одновременно входными и выходными).
# Используя четыре вызова этой функции, найти минимальное и максимальное из данных чисел A, B, C, D.

def min_max(x, y):
    if x > y:
        x , y = y, x #меняю порядок значений если x > y
    return x, y


#ввод переменных
a = input('Введи число A: ')
while type(a) != float: #обработка исключений
  try:
    a = float(a)
  except ValueError :
    print('Неправильно ввели!')
    a = input('Введите число A заново, оно должно быть нецелым: ') #пусть пользователь введёт число заново

b = input('Введи число B: ')
while type(b) != float: #обработка исключений
  try:
    b = float(b)
  except ValueError :
    print('Неправильно ввели!')
    b = input('Введите число B заново, оно должно быть нецелым: ') #пусть пользователь введёт число заново

c = input('Введи число C: ')
while type(c) != float: #обработка исключений
  try:
    c = float(c)
  except ValueError :
    print('Неправильно ввели!')
    c = input('Введите число C заново, оно должно быть нецелым: ') #пусть пользователь введёт число заново

d = input('Введи число D: ')
while type(d) != float: #обработка исключений
  try:
    d = float(d)
  except ValueError :
    print('Неправильно ввели!')
    d = input('Введите число D заново, оно должно быть нецелым: ') #пусть пользователь введёт число заново

#нахожу пары минимальных и максимальных значений
min_ab = min_max(a, b)[0]
max_ab = min_max(a, b)[1]
min_cd = min_max(c, d)[0]
max_cd = min_max(c, d)[1]

#нахожу минимум и максимум из пар
min = min_max(min_cd, min_cd)[0]
max = min_max(max_cd, max_cd)[1]
#у меня не вышло сделать это в 4 операции:(

print(f'Минимальное число: {min}\nМаксимальное число: {max}')