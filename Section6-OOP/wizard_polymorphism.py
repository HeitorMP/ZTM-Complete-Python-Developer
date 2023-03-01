class User():
    def sign_in(self):
        print('logged in')

    def attack():
        print('do nothing!')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        User.attack(self)
        print("{0} is attacking with power of {1}".format(self.name, self.power))


class Archer(User):
    def __init__(self, name, power, number_of_arrows):
        self.name = name
        self.power = power
        self.numbers_of_arrows = number_of_arrows

    def attack(self):
        print("{0} is attacking with power of {1}".format(self.name, self.power))
        print("{0} arrows left".format(self.numbers_of_arrows))


wizard1 = Wizard("Pavel Stormage", 50)
archer1 = Archer("Gungnir", 60, 15)

print(wizard1.name)
wizard1.attack()
print(wizard1.sign_in())

print(archer1.name)
archer1.attack()
print(archer1.sign_in())

print(isinstance(wizard1, Wizard))  # True
print(isinstance(wizard1, User))  # True

print(isinstance(wizard1, object))  # True


def player_attack(char):  # Polymorphism
    char.attack()


player_attack(wizard1)

print(archer1.attack())  # override de User attack
