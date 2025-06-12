#Создайте базовый класс "Животное" со свойствами "вид", "количество лап", "цвет
#шерсти". От этого класса унаследуйте класс "Собака" и добавьте в него свойства
#"кличка" и "порода".

class Animal:
    def __init__(self, species, num_paws, fur_color):
        self.species = species
        self.num_paws = num_paws
        self.fur_color = fur_color

    def print_info(self):
        print(f'Вид животного: {self.species}, количество лап: {self.num_paws}, цвет шерсти: {self.fur_color}')

class Dog(Animal):
    def __init__(self, nickname, breed, fur_color):
        self.nickname = nickname
        self.breed = breed
        super().__init__('собака', 4, fur_color)

    def print_info(self):
        print(f'Кличка собаки: {self.nickname}, порода: {self.breed}'
              f'\nВид животного: {self.species}, количество лап: {self.num_paws}, цвет шерсти: {self.fur_color}')


a = Dog('Джек', 'овчарка', 'рыже-чёрный')
a.print_info()