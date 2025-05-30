search = "Искомая строка"
found = False

try:
    with open('example.txt', 'r', encoding='utf8') as f:
        for line_num, line in enumerate(f, start = 1):
            if search in line:
                print(f'Искомая строка находится на {line_num} строке')
                found = True
        if not found:
                print('Строка не найдена')
except FileNotFoundError:
    print('Файл не существует')