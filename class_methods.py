class Gamer:
    active_gamers = 0

    @classmethod
    # '@classmethod' — это метод класса, который привязан к классу, а не к атрибуту класса
    # @classmethod - декоратор
    def get_active_gamers(cls):
        # cls — это стандартное имя первого аргумента методов класса

        return Gamer.active_gamers

    @classmethod
    def gamer_from_string(cls, data_string):
        nickname, age, level, points = data_string.split(',')
        return cls(nickname, age, level, points)

    def __init__(self, nickname, age, level, points):
        self.nickname = nickname
        self.age = age
        self.level = level
        self.points = points
        Gamer.active_gamers += 1

    def get_nickname(self):
        return self.nickname

    def get_age(self):
        return self.age

    def get_level(self):
        return self.level

    def get_points(self):
        return self.points

    def is_adult(self):
        return self.age > 18

    def get_adult_level_permission(self):
        if self.age >= 18:
            print('You can go to adult level')
        else:
            print('You can\'t go to adult level')

    def logout(self):
        Gamer.active_gamers -= 1


print(Gamer.active_gamers)
gamer_1 = Gamer('hell_boy', 23, 5, 13)
print(Gamer.active_gamers)
gamer_2 = Gamer('cool_boy', 14, 7, 25)
print(Gamer.active_gamers)

print(gamer_1.get_age())
gamer_1.get_adult_level_permission()
print(gamer_2.get_age())
gamer_2.get_adult_level_permission()

print(Gamer.active_gamers)
gamer_1.logout()

print(Gamer.active_gamers)

gamer_2.logout()

print(Gamer.active_gamers)
print(Gamer.get_active_gamers())
james = Gamer.gamer_from_string('James, 34, 56, 78')
jane = Gamer.gamer_from_string('Jane, 55, 67, 7')
jack = Gamer.gamer_from_string('Jack, 84, 67, 8')
print(james.get_age())
print(jane.get_level())
print(jack.get_points())
print(Gamer.active_gamers)

# создание словаря из списков
# встроенный класс 'dict'
a = dict.fromkeys((1, 2, 3), 'something')
print(a)
