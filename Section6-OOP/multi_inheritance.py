class User(object):
    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print("{0} is attacking with power of {1}".format(self.name, self.power))


class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def attack(self):
        print("{0} is attacking with power of {1}".format(self.name, self.power))
        print("{0} arrows left".format(self.numbers_of_arrows))

    def run(self):
        print("{} ran really fast".format(self.name))


class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)


wizard1 = Wizard("Pavel Stormage", 50)
archer1 = Archer("Gungnir", 55)
hb1 = HybridBorg("Borg", 50, 100)
print(hb1)
print(hb1.run())
