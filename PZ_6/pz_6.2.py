#2. Дан список размера N. Найти количество его промежутков монотонности
# (то есть участков, на которых его элементы возрастают или убывают).

import random

n = input('Сколько в списке будет символов? ')

while type(n) != int: #обработка исключений
  try:
    n = int(n)
  except ValueError:
    print('Неправильно ввели!')
    n = input('Введите число заново: ') #пусть пользователь введёт число заново

a = []

for i in range(n):
  a.append(random.randint(-100, 100))

if len(a) <= 1: #если в списке 1 или меньше элементов то кол-во промежутков тоже 1 или 0
  print(len(a))


def k_monotony(a):
    k = 1  # счётчик кол-ва промежутков монотонности
    monotony = None #true будет возрастающим промежутком, а false - убывающим
    for i in range(1, len(a)):
        if a[i] > a[i - 1]:  # проверяю элемент на возрастание
            if monotony == False:  # если промежуток был убывающим, то +1 к счётчику
                k += 1
            monotony = True
        elif a[i] < a[i - 1]:  # проверяю элемент на убывание
            if monotony == True:
                k += 1
            monotony = False
    return k


print('Твой список: ', a)
print('Количество промежутков монотонности в нём:', k_monotony(a))
