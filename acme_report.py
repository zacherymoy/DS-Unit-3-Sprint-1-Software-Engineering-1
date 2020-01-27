import random
namez = ['Awesome', 'Shiny', 'Impressive',
  'Portable', 'Improved']
noun = ['Anvil', 'Catapult' 'Disguise' 'Mousetrap']

class Product:

    def __init__(self, name, price =10, weight =20, flammability =0.5, identifier =random.randint(1000000,9999999)):
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

    def generate_products(name =random.choice(namez), noun = random.choice(noun),
                          price =random.randrange(5,100), weight =
                          random.randrange(5,100), flammability =random.uniform
                          (0.0,2.5), num_products=30):
        products = []
        # self.name = name
        # self.noun = noun
        # self.price = price
        # self.weight = weight
        # self.flammability = flammability
​
​
- `generate_products()` should generate a given number of products (default
  30), randomly, and return them as a list
- `inventory_report()` takes a list of products, and prints a "nice" summary