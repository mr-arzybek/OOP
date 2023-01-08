class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def names(self):
        return f"Hero name: {self.name}"

    def double_health(self):
        return self.health_points * 2

    def __str__(self):
        return f"Hero nick: {self.nickname}  Hero superpower: {self.superpower} Hero HP: { self.health_points}"

    def __len__(self):
        return len(self.catchphrase)

hero = SuperHero('Ardager', 'Dager', 'Blink', 100, "i'm Ardager")

# print(hero.names())
# print(hero.double_health())
# print(hero)
# print(len(hero.catchphrase))

# Наследование)
# Создать 2 класса наследованных от класса SuperHero
# Все эти классы это герои своей местности(воздушные, земные ,космические и тд)
#
#
#  к каждому классу добавить
# Свой атрибут на уровне класса.
# И новые аргументы damage и  fly который по УМОЛЧАНИЮ будет равен False
#
# (полиморфизм)
# У каждого класса наследованных от Hero
# Изменить метод который умножал хп героев на 2
# теперь он должен возводить его в квадрат и меняет значение параметра fly на True
#
# создать новый метод который
#  выводит фразу fly in the True_phrase
#
# создать объекты у новых классов
# и вызвать новые методы
#
# создать класс villain наследованный от нового класса
# изменить  значение  атрибутa people на monster
#
# создать метод gen_x который ПОКА ничего не делает
#
# создать метод crit который возводит в степень урон
#
# создать объекты для этого класса
#
# применить метод crit на объект другого класса  у которого есть аргумент damage
#
# дз принимаю только гитом (не забудьте про gitignore)

class AirHR(SuperHero):
    def __int__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False):
        SuperHero.__init__(self, name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def double_health(self):
        print(f'HP {self.name} x2: {self.health_points * self.health_points}')
        self.fly = True

    def fly_phrase(self):
        if self.fly_phrase:
            print(f'fly in the True_phrase')

aang = AirHR(f'Aang', f'Ang', f'up_kick', 15, "I'm still young to die!")
print(aang.double_health())
print(aang.fly)
print(aang.fly_phrase())



class EarthlyHR(SuperHero):
    def __int__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False):
        SuperHero.__init__(self, name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly
    def __int__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False):
        super().__init__(self, name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def double_health(self):
        print(f'HP {self.name} x2: {self.health_points * self.health_points}')
        self.fly = True

    def fly_phrase(self):
        if self.fly_phrase:
            print(f'fly in the True_phrase')

toph = EarthlyHR(f'Toph', f'Tooph', f'midle_kick', 17, "Come here and I'll wipe the grin off your faces!")
print(toph.double_health())
print(toph.fly)
print(toph.fly_phrase())



class Villain(EarthlyHR):
    people = 'monster'
    def gen_x(self):
        pass
    def crit(self):
        self.damage **= 2
        return self.damage

print(EarthlyHR.damage)



