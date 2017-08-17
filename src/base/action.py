from enum import Enum
import weapon

class Type(Enum):
    MELEEWEAPON, RANGEDWEAPON, SPECIAL = range(3)

class Action:
    def __init__(self,  user, name="Club"):
        self.name = name
        self.type = Type.MELEEWEAPON
        self.weapon = weapon.Weapon("Club")
        self.special = None
        self.user = user

    def __str__(self):
        STR = self.user.abilities.STR
        DEX = self.user.abilities.DEX
        prof = self.user.prof

        if self.type is Type.MELEEWEAPON:
            stat = STR
            reach = self.weapon.reach
            damage = self.weapon.damage
            dice = self.weapon.dice

            if weapon.Property.FINESSE in self.weapon.properties:
                stat = DEX
            if weapon.Property.TWOHANDED in self.weapon.properties:
                dice = self.weapon.alternate
            if weapon.Property.VERSATILE in self.weapon.properties and len(user.wield) < 2:
                dice = self.weapon.alternate

            return "<p><i><b>{}</b>. Melee Weapon Attack:</i> {:+} to hit, reach {} ft., one target. <i>Hit</i>: {} ({}) {} damage.</p>".format(self.name, (stat - 10) // 2 + prof, reach,
                dice.avg + (stat - 10) // 2, dice, damage)

        elif self.type is Type.RANGEDWEAPON:
            stat = DEX
            reach = 5
            primary = self.weapon.reach
            secondary = self.weapon.secondary
            damage = self.weapon.damage
            dice = self.weapon.dice

            if weapon.Property.THROWN in self.weapon.properties:
                stat = STR
            if weapon.Property.AMMUNITION in self.weapon.properties:
                pass # todo
            if weapon.Property.LOADING in self.weapon.properties:
                pass # todo

            return "{}. Ranged Weapon Attack: {:+} to hit, range {} ft., one target. Hit: {} ({}) {} damage.".format(self.name, (stat - 10) // 2 + prof, reach,
                dice.avg + (stat - 10) // 2, dice, damage)

        else:
            return "todo"
