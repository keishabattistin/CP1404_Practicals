
class Guitar:
    def __init__(self, name='', year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost
        self.vintage = ''
        self.age = 0
        self.is_vintage()

    def get_age(self):
        self.age = 2017 - self.year

    def is_vintage(self):
        self.get_age()
        if self.age >= 50:
            self.vintage = '(vintage)'

    def __str__(self):

        return '{} ({}) : $ {:10,.2f} {}'. format(self.name, self.year, self.cost, self.vintage)