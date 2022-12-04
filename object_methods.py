class Human:
    position = 'waiter'

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def work_experience(self, last_job):
        print(self.last_name + ' had work experience ' + last_job)

    def __str__(self):
        # '__str__ вызывается в случаях преобразования атрибута класса к строке
        return f'{self.first_name}({self.age})'


employee_1 = Human('Nick', 'Smith', 18)
employee_1.work_experience('KFS')
print(employee_1)
employee_2 = Human('Kate', 'Brown', 45)
employee_2.work_experience('Dodo')
print(employee_1.position, employee_1.first_name, employee_1.last_name, employee_1.age)


class Animals:
    kind_of_animal = 'pet'

    def __init__(self, name, color, tail):
        self.name = name
        self.color = color
        self.tail = tail

    # методов может быть множество
    def sound(self, sing):
        print(self.name, 'sound so loud ', sing)

    def change_color(self, new_color):
        self.color = new_color


animal_1 = Animals('dog', 'black', True)
animal_1.sound(False)
animal_2 = Animals('cat', 'white', True)
animal_2.sound(False)
animal_1.change_color('pink')
print(animal_1.kind_of_animal, animal_1.name, animal_1.color, animal_1.tail)
print(animal_2.kind_of_animal, animal_2.name, animal_2.color, animal_2.tail)


class Circle:
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
        self.perimeter = 2 * Circle.pi * self.radius

    def get_area(self):
        return self.pi * (self.radius ** 2)

    def get_circumference(self):
        return 2 * self.pi * self.radius


circle_1 = Circle()
print(circle_1.get_area())
print(circle_1.get_circumference())
print(circle_1.perimeter)
circle_2 = Circle(4)
print(circle_2.get_area())
print(circle_2.get_circumference())
circle_3 = Circle(5)
a = circle_3.get_area()
b = circle_3.get_circumference()
print(a)
print(b)


class Birds:
    pass
# если класс пустой, чтобы избежать ошибки ставим 'pass'
