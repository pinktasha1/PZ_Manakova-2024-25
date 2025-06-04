#В исходном текстовом файле(Dostoevsky.txt) найти все фамилии с инициалами
#(например, А. Ф. Куманиной и т.п.).

import re

with open("Dostoevsky.txt", "r", encoding="utf-8") as f:
    text = f.read()

find = r'\b[А-ЯЁ]\.\s?[А-ЯЁ]\.\s?[А-ЯЁа-яё]+'

matches = re.findall(find, text)

print("Найденные фамилии с инициалами:")
for i in matches:
    print(i)