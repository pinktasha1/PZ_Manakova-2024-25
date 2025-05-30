#2. Из предложенного текстового файла (text18-10.txt) вывести на экран его содержимое,
# количество букв в верхнем регистре. Сформировать новый файл, в который поместить текст
# в стихотворной форме предварительно поставив после последней строки автора и название произведения.

with open("text18-10.txt", "r", encoding="utf-8") as f:
    poem = f.read()

uppercase_count = sum(1 for char in poem if char.isupper())

print(f"""Содержимое файла:\n{poem}\n
Количество букв в верхнем регистре: {uppercase_count}""")

autor = 'Михаил Юрьевич Лермонтов'
title = 'Бородино'

new_text = poem.strip() + f"\n\nАвтор: {autor}\nПроизведение: {title}"

with open("new_text18-10.txt", "w", encoding="utf-8") as f:
    f.write(new_text)

f.close()