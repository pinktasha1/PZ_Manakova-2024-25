def last_direct(file_path):
    parts = file_path.split('\\') #Разделяем путь на части по символу '\'
    last_dir = parts[-2] #Предпоследняя часть - название каталога
    return last_dir


print(last_direct(input('Полное имя файла: ')))