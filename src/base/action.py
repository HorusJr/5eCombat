from enum import Enum
import weapon

class Type(Enum):
    MELEEWEAPON, RANGEDWEAPON, SPECIAL = range(3)

class Action:
    def __init__(self, name="Club"):
        self.name = name
        self.type = Type.MELEEWEAPON
        self.weapon = weapon.Weapon("Club")
        self.special = None

    def __str__(self):
        STR = 10
        DEX = 10
        prof = 2

        if self.type is Type.MELEEWEAPON:
            hit = (STR - 10) // 2 + prof
            reach = 5
            damage = self.weapon.dice.avg
            dice = str(self.weapon.dice)
            dtype = self.weapon.damage

            if weapon.Property.FINESSE in self.weapon.properties:
                tohit = (DEX - 10) // 2 + prof
            else:
                tohit = (STR - 10) // 2 + prof

            return "{}. Melee Weapon Attack: {:+} to hit, reach {} ft., one target. Hit: {} ({}) {} damage.".format(self.name, hit, reach, damage, dice, dtype)

        else:
            return "nah"

if __name__ == "__main__":
    print(Action())
