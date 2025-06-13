#Создайте класс "Здание" с атрибутами "адрес" и "количество этажей". Напишите
#метод, который выводит информацию о здании в формате "Адрес: адрес, Количество
#этажей: этажи".

class Zdanie:
    def __init__(self, address, num_floors):
        self.address = address
        self.num_floors = num_floors
    def print_address(self):
        print(f'Адрес: {self.address}, количество этажей: {self.num_floors}')

a = Zdanie('Королёва 12/3', 3)
a.print_address()