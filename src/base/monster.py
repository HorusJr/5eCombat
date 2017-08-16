import random
from enum import Enum
from collections import *

class Size(Enum):
    TINY, SMALL, MEDIUM, LARGE, HUGE, GARGANTUAN = range(6)

class Type(Enum):
    ABERRATION, BEAST, CELESTIAL, CONSTRUCT, DRAGON, ELEMENTAL, FEY, FIEND, GIANT, HUMANOID, MONSTROSITY, OOZE, PLANT, UNDEAD = range(14)

class Alignment(Enum):
    LAWFULGOOD, NEUTRALGOOD, CHAOTICGOOD, LAWFULNEUTRAL, TRUENEUTRAL, CHAOTICNEUTRAL, LAWFULEVIL, NEUTRALEVIL, CHAOTICEVIL = range(9)

class Language(Enum):
    COMMON, DWARVISH, ELVISH, GIANT, GNOMISH, GOBLIN, ORC, ABYSSAL, CELESTIAL, DEEPSPEECH, DRACONIC, INFERNAL, PRIMORDIAL, SYLVAN, UNDERCOMMON, DRUIDIC, ARAKOCRA, \
    BLINKDOG, BULLYWUG, GIANTEAGLE, GIANTELK, GIANTOWL, GITH, GNOLL, GRELL, HOOKHORROR, MODRON, OTYUGH, SLAAD, SPHINX, THRIKEEN, TROGLODYTE, UMBERHULK, WINTERWOLF, \
    WORG, YETI = range(36)

Abilities = namedtuple('Ability', ['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA'])

class Monster:
    def __init__(self, name="Commoner"):
        self.name = name
        self.size = Size.MEDIUM
        self.type = Type.HUMANOID
        self.tags = ("human")
        self.alignment = random.choice(list(Alignment))
        self.ac = 10
        self.hp = 4
        self.abilities = Abilities(10,10,10,10,10,10)
        self.speed = {'speed': 30}
        self.skills = {}
        self.throws = Abilities(0,0,0,0,0,0)
        self.vulnerabilities = ()
        self.resistances = ()
        self.immunities = ()
        self.senses = {'vision': -1}
        self.languages = (Language.COMMON)
        self.cr = 0

        self.armor = ()
        self.weapons = ()
        self.equipment = ()
