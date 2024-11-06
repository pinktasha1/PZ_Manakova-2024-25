#1. Дано целое число N (> 0). Найти сумму N^2 + (N + 1)^2 + (N + 2)^2 + ... + (2N)^2

a = input('Введи число n: ')

while type(a) != int: #обработка исключений
  try:
    a = int(a)
    if a <= 0:
        raise ValueError
  except ValueError :
    print('Неправильно ввели!')
    a = input('Введите первое число: ') #пусть пользователь введёт число заново

def sum_squares(a):
  total_sum = 0
  n = a
  while n <= 2 * a:
      total_sum += n ** 2
      n += 1
  return total_sum
total_sum = sum_squares(a)

print (f'Сумма квадратов от {a} до {2 * a}: {total_sum}')
