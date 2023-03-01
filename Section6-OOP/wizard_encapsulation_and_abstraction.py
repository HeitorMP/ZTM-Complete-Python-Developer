# INHERITANCE

class PlayerCharacter():
    membership = True  # Class Object Attribute

    def __init__(self, name, pclass):  # Constructor function
        if PlayerCharacter.membership:
            # Private conevention var names: _varname
            self._name = name
            self._pclass = pclass

    def run(self):
        print("run")

    def shout(self):
        print("My name is {0} and I am a {1}".format(self._name, self._pclass))

    @classmethod  # Decorator
    def adding_things(cls, num1, num2):
        return cls('Lala', num1 + num2)

    @staticmethod
    def adding_things_static(num1, num2):
        return num1 + num2


player1 = PlayerCharacter("Gungnir", "Warrior")
player2 = PlayerCharacter("Stormage", "Mage")

player1.attack = 50

print(player1._name)
print(player1._pclass)
print(player2._name)
print(player2._pclass)

print(player1.attack)
print(player2.membership)

player2.membership = False
print(player2.membership)

player2.shout()

player3 = PlayerCharacter.adding_things(2, 3)
print(player3._name)
player3.shout()
print(player3.adding_things_static(2, 2))
