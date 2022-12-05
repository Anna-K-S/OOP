class Person:
    def __init__(self, first_name, last_name, age):
        # ''__init__()' - инициализотор класса
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        # '__str__()' - переопределяет метод, возвращая строковое значение
        return self.first_name + ' ' + self.last_name

    def __len__(self):
        return self.age

    def __del__(self):
        # '__del__' - деструктор
        # __del__ всегда вызывается по завершении работы интерпретатора
        print('Person object with name', self.first_name,
              'is deleted from memory')

    def __add__(self, other):
        # '__add__()' - используется для сложения атрибутов объекта
        return self.age + other.age


# jack = Person.__str__(('Jack', 'Brown', 25))
jack = Person('Jack', 'Brown', 25)
jane = Person('Jane', 'White', 34)
print(jane + jack)

print(len([1, 2, 3, 4, 5, 6, 7]))
print(jack)
print(len(jack))
# del jack


x = 5
y = 3

a = '5'
b = '3'

print(x.__add__(y))
print(a.__add__(b))

# Некоторые другие арифмитические методы
''' __sub__() — Вычитание;
__mul__() — Умножение;
__truediv__() — Деление (x/y);
__floordiv__() — Целочисленное деление (x // y);
__mod__() — Остаток от деления;
__pow__() — Возведение в степень'''