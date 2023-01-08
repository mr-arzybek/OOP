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

print(hero.names())
print(hero.double_health())
print(hero)
print(len(hero.catchphrase))
