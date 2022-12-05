# # Inheritance
#
class Pizza:
    size = 30

    def __init__(self, name, sauce, meat, cheese, vegetable_1, vegetable_2):
        self.name = name
        self.sauce = sauce
        self.meat = meat
        self.cheese = cheese
        self.vegetable_1 = vegetable_1
        self.vegetable_2 = vegetable_2
        print('Pizza is ready')

    def slice(self, number_od_slices):
        print(self.name, 'has cut into', number_od_slices, 'slices')

    def change_meat(self, new_meat):
        self.meat = new_meat
        print('Meat is changed to', new_meat)


class Pie(Pizza):
    size = 25

    def __init__(self, name, sauce, meat, cheese, vegetable_1, vegetable_2):
        Pizza.__init__(self, name, sauce, meat, cheese,
                       vegetable_1, vegetable_2)
        print('Pie is ready')

    def slice(self, number_od_slices):
        print('Pie', self.name, 'has cut into', number_od_slices, 'slices')

    def cooking_time(self, in_the_oven):
        print('Cooking time in the oven is', in_the_oven, 'min')


meat_pie = Pie('Aussie pie', 'red', 'beef', 'parmesan',
               'onion', 'carrot')

meat_pie.slice(9)
print(meat_pie.size)
print(meat_pie.meat)
meat_pie.change_meat('chicken')
print(meat_pie.meat)
meat_pie.cooking_time(45)

# Polymorphism
# медоты с одинаковыми названием и пораметрами ведут себя по разному

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError('Class successor must implement'
                                  ' this method')


class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name, 'is saying "woof"')


class Cat(Animal):
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name, 'is saying "meow"')


class Mouse(Animal):
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name, 'is saying "pee-pee-pee"')


class Fish(Animal):
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name, 'is saying nothing')


spike = Dog('Spike')
tom = Cat('Tom')
jerry = Mouse('Jerry')
nemo = Fish('Nemo')
pet_list = [spike, tom, jerry, nemo]

for pet in pet_list:
    pet.speak()


def pet_voice(pet):
    pet.speak()


pet_voice(spike)
pet_voice(tom)
pet_voice(jerry)
pet_voice(nemo)

