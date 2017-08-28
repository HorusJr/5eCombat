from enum import Enum
import dice

class Property(Enum):
    AMMUNITION, FINESSE, HEAVY, LIGHT, LOADING, SPECIAL, THROWN, TWOHANDED, VERSATILE, NET = range(10)

class Weapon:
    def __init__(self, name="Club"):
        self.name = name
        self.cost = 500
        self.dice = dice.Dice(1,6)
        self.alternate = None
        self.reach = 5
        self.secondary = None
        self.weight = 4
        self.properties = (Property.LIGHT, )
        self.damage = "bludgeoning"
