def concatenate():
    animals = {'Tiger': 67, 'Lion': 89, 'Leopard': 35}
    birds = {'Parrot': 58, 'Eagle': 79, 'Sparrow': 45}
    food = {'Pizza':20, 'Pasta': 25, 'Burger': 10}
    new_d = {**animals, **birds, **food}
    print(new_d)

concatenate()
