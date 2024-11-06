#1. Дано целое число N (> 0). Найти сумму N^2 + (N + 1)^2 + (N + 2)^2 + ... + (2N)^2
from tkinter.font import names

n = input('Введи число n: ')

while type(n) != int: #обработка исключений
  try:
    n = int(n)
    if n <= 0:
        raise ValueError
  except ValueError :
    print('Неправильно ввели!')
    n = input('Введите первое число: ') #пусть пользователь введёт число заново

def sum_squares(a):
  total_sum = 0
  a = n
  while a <= 2 * n:
      total_sum += a ** 2
      a += 1
  return total_sum
total_sum = sum_squares(n)

print (f'Сумма квадратов от {n} до {2 * n}: {total_sum}')
