#2. Из заданной строки отобразить только цифры. Использовать библиотеку string.
#Строка - TheGreatPyramidofKhufuatGizawasbuiltabout 2700 BC, 755 feet (230metres) longand
#481 feet (147 metres) high.

import string

n = "TheGreatPyramidofKhufuatGizawasbuiltabout 2700 BC, 755 feet (230metres) longand  481 feet (147 metres) high."

digits = ''.join([char for char in n if char in string.digits])

print(digits)