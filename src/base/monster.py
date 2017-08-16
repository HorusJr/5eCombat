from enum import Enum

class Monster:
    def __init__(self, name="Commoner"):
        self.name = name
        self.size = "Medium"
        self.type = "humanoid"
        self.tags = ("human")
        self.alignment = "true neutral"
        self.ac = 10
        self.hp = 4
        self.speed = {'speed': 30, 'burrow': 0, 'climb': 15, 'fly': 0, 'swim': 15}
        self.saving = ['STR': 10, 'DEX': 10, 'CON': 10, "INT": 10, "WIS": 10, "CHA": 10]
        self.skills = ['athletics': 0, 'acrobatics': 0, 'sleight': 0, 'stealth': 0, 'arcana': 0, 'history': 0, 'investigation': 0, 'nature': 0, 'religion': 0 \
            'animal': 0, 'insight': 0, 'medicine': 0, 'perception': 0, 'survival': 0, 'deception': 0, 'intimidation': 0, 'performance': 0, 'persuasion': 0]
        self.saving = ['STR': 0, 'DEX': 0, 'CON': 0, "INT": 0, "WIS": 0, "CHA": 0]
        self.vulnerabilities = ()
        self.resistances = ()
        self.immunities = ()
        self.senses = {}
        self.languages = ("Common")
        self.cr = 0

        self.armor = ()
        self.weapons = (Weapon())
        self.equipment = ()
