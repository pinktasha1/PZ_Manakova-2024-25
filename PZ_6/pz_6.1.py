#1. Дан список A размера N и целое число K (1 < K < N). Вывести элементы список с порядковыми номерами,
# кратными K: AK, A2*K, A3*K,... . Условный оператор не использовать.

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

k = input('Придумай число не больше 10: ')
while type(k) != int: #обработка исключений
  try:
    k = int(k)
    if k >= 10:
      raise ValueError('Число должно быть больше 10')
  except ValueError :
    print('Неправильно ввели!')
    k = input('Введите число заново: ') #пусть пользователь введёт число заново

result = []

for i in range(0, 10, k): #перебираю список с интервалом равным k
  result.append(i)

del result[0] #убираю ноль
print(result)