from acme import Product
import random
from random import randint, sample, uniform

def generate_products():
    namez = ['Awesome', 'Shiny', 'Impressive',
    'Portable', 'Improved']
    noun = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap']
    random_30 = []
    for i in range(30):
        prod_name = random.choice(namez) + ' ' + random.choice(noun)
        random_30.append(prod_name)
    return random_30

def inventory_report():

    random_numbers = [random.randint(5, 100) for i in range(30)]
    average_price = sum(random_numbers)/len(random_numbers)

    random_weight = [random.randint(5, 100) for i in range(30)]
    average_weight = sum(random_weight)/len(random_weight)

    random_flammability = [random.uniform(0.0,2.5) for i in range(30)]
    average_flammability = sum(random_flammability)/len(random_flammability)

    product1 = Product(name = random.choice(generate_products),
                           weight = random.choice(random_weight,
                           flammability = random.choice)) #This will return list of 30.
    #price1

    if __name__ == '__main__':
    inventory_report(generate_products())
