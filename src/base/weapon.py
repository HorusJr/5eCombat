from enum import Enum
import dice

class Property(Enum):
    AMMUNITION, FINESSE, HEAVY, LIGHT, LOADING, RANGE, REACH, SPECIAL, THROWN, TWOHANDED, VERSATILE, SILVERED, LANCE, NET = range(14)

class Weapon:
    def __init__(self, name="Club"):
        self.name = name
        self.cost = 500
        self.dice = dice.Dice(1,6)
        self.weight = 4
        self.properties = (Property.LIGHT, )
        self.damage = "bludgeoning"
