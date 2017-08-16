from enum import Enum
from collections import *
import random, uuid, os, webbrowser
import action, weapon

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
        self.prof = 2
        self.abilities = Abilities(10,10,10,10,10,10)
        self.speed = {'speed': 30}
        self.skills = {}
        self.throws = Abilities(0,0,0,0,0,0)
        self.vulnerabilities = ()
        self.resistances = ()
        self.immunities = ()
        self.senses = {'vision': -1}
        self.languages = (random.choice(list(Language)))
        self.cr = 0

        self.armor = ()
        self.weapons = ()
        self.equipment = ()
        self.wield = (weapon.Weapon())

        self.actions = (action.Action(self), )

        self.url =  "../../sites/{}.html".format(uuid.uuid4().int)

    def gen_website(self):
        f = open(self.url, 'w')

        body = '''
<html>
<head>
  <title>Commoner</title>
  <link rel="stylesheet" href="monster.css" />
</head>

<body>
  <div id="wrapper">
    <div id="header">
      <h2>COMMONER</h2>
      <p>Medium humanoid (human), true neutral</p>
    </div>

    <div id="ac">
      <p><b>Armor Class</b> 10</p>
      <p><b>Hit Points</b> 4 (1d8)</p>
      <p><b>Speed</b> 30 ft.</p>
    </div>

    <div id="abilities">
      <div class="ability">
        <div class="top">
          STR
        </div>
        10 (+0)
      </div>
      <div class="ability">
        <div class="top">
          DEX
        </div>
        10 (+0)
      </div>
      <div class="ability">
        <div class="top">
          CON
        </div>
        10 (+0)
      </div>
      <div class="ability">
        <div class="top">
          INT
        </div>
        10 (+0)
      </div>
      <div class="ability">
        <div class="top">
          WIS
        </div>
        10 (+0)
      </div>
      <div class="ability">
        <div class="top">
          CHA
        </div>
        10 (+0)
      </div>
    </div>

    <div id="extras">
      <p><b>Senses</b> passive Perception 10</p>
      <p><b>Languages</b> Common</p>
      <p><b>Challenge</b> 0</p>
    </div>

    <div id="special"></div>

    <div id="actions">
      <h3>Actions</h3>
      <p><i><b>Club.</b> Melee Weapon Attack:</i> +2 to hit, reach 5 ft., one
        target. <i>Hit:</i> 2 (1d4) bludgeoning damage.
    </div>

    <div id="legendary">

    </div>

  </div>
<body>

</html>

        '''

        f.write(body)
        f.close()

    def show_website(self):
        if not os.path.exists(self.url):
            self.gen_website()

        webbrowser.open('file://' + os.path.realpath(self.url))


if __name__ == "__main__":
    Bob = Monster("Commoner")
    Bob.show_website()
