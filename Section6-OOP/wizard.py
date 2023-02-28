class PlayerCharacter:
    membership = True  # Class Object Attribute

    def __init__(self, name, p_class):  # Constructor function
        if PlayerCharacter.membership:
            self.name = name
            self.p_class = p_class

    def run(self):
        print("run")

    def shout(self):
        print("My name is {}".format(self.name))


player1 = PlayerCharacter("Gungnir", "Warrior")
player2 = PlayerCharacter("Stormage", "Mage")

player1.attack = 50

print(player1.name)
print(player1.p_class)
print(player2.name)
print(player2.p_class)

print(player1.attack)
print(player2.membership)

player2.membership = False
print(player2.membership)

player1.shout()
