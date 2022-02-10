# by Kami Bigdely
# Consolidate duplicate conditional fragments

def add(mix, *argv):
    for item in argv:
        mix.append(item)
    return mix


def make_drink(drink, *argv):
    mix = []

    if 'coffee' in drink:
        add(mix, 'coffee')
    elif 'strawberry milkshake' in drink:
        add(mix, 'ice', 'cream', 'strawberry')

    mix = add(mix, *argv)

    return mix


final_drink = make_drink('strawberry milkshake', 'milk', 'sugar')
print(final_drink)
