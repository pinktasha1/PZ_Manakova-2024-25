#2. Дан номер месяца — целое число в диапазоне 1-12 (1 — январь, 2 — февраль и т. д.). Определить количество дней в этом месяце для невисокосного года.

month = {'1':'31','2':'28','3':'31','4':'30','5':'31','6':'30','7':'31','8':'31','9':'30','10':'31','11':'30','12':'31'}

a = input('Введите число от 1 до 12. Оно будет номером месяца: ')

while type(a) != int: #обработка исключений
  try:
    a = int(a)
    if 1 <= a <= 12: #диапазон от 1 до 12
      print('В этом месяце', month.get(str(a)), 'дней.')
    else:
      print('Число должно быть от 1 до 12.')
      a = input("Введите число заново: ") #пусть пользователь введёт число заново
  except ValueError:
    print('Неправильно ввели!')
    a = input("Введите число заново: ") #пусть пользователь введёт число заново
