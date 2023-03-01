class User(object):
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power, email):
        User.__init__(self, email)  # calling the __init__ from User class
        self.name = name
        self.power = power

    def attack(self):
        print("{0} is attacking with power of {1}".format(self.name, self.power))


class Archer(User):
    def __init__(self, name, power, number_of_arrows, email):
        # calling the User but no need to pass itself, more clean with super()
        super().__init__(email)
        self.name = name
        self.power = power
        self.numbers_of_arrows = number_of_arrows

    def attack(self):
        print("{0} is attacking with power of {1}".format(self.name, self.power))
        print("{0} arrows left".format(self.numbers_of_arrows))


wizard1 = Wizard("Pavel Stormage", 50, 'pavel@protonmail.com')
archer1 = Archer("Gungnir", 55, 15, 'gungao_da_massa64@hotmail.com')
print(wizard1.email)
print(archer1.email)
