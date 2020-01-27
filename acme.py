import random
class Product:

    def __init__(self, name, price=10, weight=20, flammability=0.5, identifier=random.randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        # print(f"if the ratio is less than 0.5 return 'Not so stealable...',"
        # "if it is greater or equal to 0.5 but less than 1.0 return 'Kinda stealable.',"
        # "and otherwise return 'Very stealable!'")
        print(f"Kinda stealable.")
        return self.price / self.weight

    def explode(self):
        # print(f'if the product is less than 10 return "...fizzle.", if it is'
        # 'greater or equal to 10 but less than 50 return "...boom!", and otherwise'
        # 'return "...BABOOM!!"')
        print(f'...boom!')
        return self.flammability * self.weight

    class BoxingGlove(Product):
        def __init__(self, name, price=10, weight=10, flammability=0.5, identifier=random.randint(1000000, 9999999)):
            self.weight = weight
            super().__init__(name, price=10, weight=10, flammability=0.5, identifier=random.randint(1000000, 9999999))

        def explode(self):
            print("...it's a glove.")

        def punch(weight):
            print("'Hey that hurt!'")
            # if weight < 5:
            #   print("That tickles.")
            # elif 5>= weight <15:
            #   print("Hey that hurts!")
            # else:
            #   print("Ouch!")