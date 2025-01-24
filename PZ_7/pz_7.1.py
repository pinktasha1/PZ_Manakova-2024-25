#Дана строка. Вывести строку, содержащую те же символы, но расположенные в обратном порядке.
def reverse(a):
    return a[::-1]


string = (input('Введите строку: '))

new_list = reverse(string)
print(new_list)