# (03.03.26)
# This program defines a Character class with methods to show health and take damage

class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def show_health(self):
        print("Health:", self.health)
#improved version of the show_health method to include the character's 
    def show_health(self):
        print(self.name, "has", self.health, "health")

    def take_damage(self, amount):
        self.health = self.health - amount


player = Character("King", 100)

player.take_damage(30)
player.show_health()


