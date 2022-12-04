class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("John", 36)

print(p1.name)
print(p1.age)


class Car:
    wheels_number = 4

    # значение одинаковое для всех объектов создается на уровне класса
    def __init__(self, name, color, year, is_crashed):
# '__init__' - встроенный метод конструктор класса
# 'self' - это стандартное имя первого аргумента для методов объекта
        self.name = name
        self.color = color
        self.year = year
        self.is_crashed = is_crashed


mazda_car = Car(name='Mazda CX7', color='Black', year=2010, is_crashed=True)
bmw_car = Car('BMW X7', 'White', 2019, False)
print(mazda_car.name, mazda_car.color, mazda_car.year, mazda_car.is_crashed, mazda_car.wheels_number)
print(bmw_car.name, bmw_car.color, bmw_car.year, bmw_car.is_crashed, bmw_car.wheels_number)

number_of_wheels_of_3_cars = Car.wheels_number * 3
print(number_of_wheels_of_3_cars)
