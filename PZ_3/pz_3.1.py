#1. Даны два целых числа: A, B. Проверить истинность высказывания: «Ровно одно из чисел A и B нечетное».

a = input('Введите число A: ')
b = input('Введите число B: ')

while type(a) != int: #обработка исключений
  try:
    a = int(a)
  except ValueError:
    print('Неправильно ввели!')
    a = input('Введите число A: ') #пусть пользователь введёт число заново

while type(b) != int: #обработка исключений
  try:
    b = int(b)
  except ValueError:
    print('Неправильно ввели!')
    b = input('Введите число B: ') #пусть пользователь введёт число заново

print('Ровно одно из чел A и B нечётное?')
if (a % 2 == 0 and b % 2 != 0) or (a % 2 != 0 and b % 2 == 0):
  print('True')
else:
  print('False')
print('Программа завершена.')
