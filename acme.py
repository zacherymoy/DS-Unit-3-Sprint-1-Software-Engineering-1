import random
class Product:

    def __init__(self, name, price=10, weight=20, flammability=0.5, identifier=random.randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        x = self.price / self.weight
        if x < 0.5:
            print(f'Not so stealable...')
        elif x >= 0.5 and x < 1.0:
            print(f'Kinda stealable.')
        else:
            print(f'Very stealable!')

    def explode(self):
        y = self.flammability * self.weight
        if y < 10:
            print(f'...fizzle')
        elif y >= 10 and y < 50:
            print(f'...boom!')
        else:
            print(f'....boom!')

class BoxingGlove(Product):

        def __init__(self, name, price=10, weight=10, flammability=0.5, identifier=random.randint(1000000, 9999999)):
            self.weight = weight
            super().__init__(name, price=10, weight=10, flammability=0.5, identifier=random.randint(1000000, 9999999))

        def explode(self):
            print("...it's a glove.")

        def punch(weight):
            print("'Hey that hurt!'")
            if weight < 5:
              print("That tickles.")
            elif weight >= 5 and weight <15:
              print("Hey that hurts!")
            else:
              print("Ouch!")
