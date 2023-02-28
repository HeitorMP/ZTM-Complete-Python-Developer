# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats

cat1 = Cat('Felix', 104)
cat2 = Cat('Tom', 83)
cat3 = Cat('Sylvester', 71)

# 2 Create a function that finds the oldest cat


def oldest_cat(*args):
    age_list = []
    for cat in args:
        age_list.append(cat.age)
    return max(age_list)

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2


print(oldest_cat(cat1, cat2, cat3))

# Official Solution

"""
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Instantiate the Cat object with 3 cats
peanut = Cat("Peanut", 3)
garfield = Cat("Garfield", 5)
snickers = Cat("Snickers", 1)


# Find the oldest cat
def get_oldest_cat(*args):
    return max(args)


# Output
print(f"The oldest cat is {get_oldest_cat(peanut.age, garfield.age, snickers.age)} years old.")
"""
