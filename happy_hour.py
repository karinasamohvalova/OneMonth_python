import random

clothes = ["Trousers",
        "Skirt",
        "Shirt",
        "Boots",
        "Dress"]

colour = ["Red",
          "White",
          "Pink",
          "Yellow",
          "Black",
          "Orange"]

random_clothes = random.choice(clothes)
random_colour_one = random.choice(colour)
random_colour_two = random.choice(colour)

print(f"How about you to put on {random_clothes} coloured in {random_colour_one} and {random_colour_two}?")
