class Hero:

    def __init__(self, name, abillity):
        self.name = name
        self.abillity = abillity

class Hero_super(Hero):

    def __str__(self):
        return f'{self.name}, {self.abillity}'

    def nick(self):
        print(f'{self.name} - it is superhero')