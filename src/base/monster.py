from enum import Enum
from collections import *
import random, uuid, os, webbrowser, time
import action, weapon, dice

class Size(Enum):
    TINY, SMALL, MEDIUM, LARGE, HUGE, GARGANTUAN = range(6)

class Type(Enum):
    ABERRATION, BEAST, CELESTIAL, CONSTRUCT, DRAGON, ELEMENTAL, FEY, FIEND, GIANT, HUMANOID, MONSTROSITY, OOZE, PLANT, UNDEAD = range(14)

class Alignment(Enum):
    LAWFUL_GOOD, NEUTRAL_GOOD, CHAOTIC_GOOD, LAWFUL_NEUTRAL, TRUE_NEUTRAL, CHAOTIC_NEUTRAL, LAWFUL_EVIL, NEUTRAL_EVIL, CHAOTIC_EVIL = range(9)

class Language(Enum):
    COMMON, DWARVISH, ELVISH, GIANT, GNOMISH, GOBLIN, ORC, ABYSSAL, CELESTIAL, DEEP_SPEECH, DRACONIC, INFERNAL, PRIMORDIAL, SYLVAN, UNDERCOMMON, DRUIDIC, AARAKOCRA, \
    BLINK_DOG, BULLYWUG, GIANT_EAGLE, GIANT_ELK, GIANT_OWL, GITH, GNOLL, GRELL, HOOK_HORROR, MODRON, OTYUGH, SLAAD, SPHINX, THRIKEEN, TROGLODYTE, UMBERHULK, \
    WINTER_WOLF, WORG, YETI = range(36)

class Speed(Enum):
    BURROW, CLIMB, FLY, SWIM = range(4)

class Sense(Enum):
    BLINDSIGHT, DARKVISION, TREMORSENSE, TRUESIGHT = range(4)

class Skill(Enum):
    ATHLETICS, ACROBATICS, SLEIGHT_OF_HAND, STEALTH, ARCANA, HISTORY, INVESTIGATION, NATURE, RELIGION, ANIMAL_HANDLING, INSIGHT, MEDICINE, PERCEPTION, SURVIVAL, \
    DECEPTION, INTIMIDATION, PERFORMANCE, PERSUASION = range(18)

Abilities = namedtuple('Ability', ['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA'])
alignments = ["lawful good", "neutral good", "chaotic good", "lawful neutral", "true neutral", "chaotic neutral", "lawful evil", "neutral evil", "chaotic evil"]

class Monster:
    def __init__(self, name="Commoner"):
        self.name = name
        self.size = Size.MEDIUM
        self.type = Type.HUMANOID
        self.tags = ("human", )
        self.alignment = random.choice(list(Alignment))
        self.ac = 10
        self.hp = dice.Dice(1, 8)
        self.prof = 2
        self.abilities = Abilities(10,10,10,10,10,10)
        self.speed = {'speed': 30}
        self.skills = {}
        self.throws = Abilities(0,0,0,0,0,0)
        self.vulnerabilities = ()
        self.resistances = ()
        self.immunities = ()
        self.senses = {}
        self.languages = (random.choice(list(Language)), )
        self.cr = 0

        self.armor = ()
        self.weapons = ()
        self.equipment = ()
        self.wield = (weapon.Weapon(), )

        self.actions = (action.Action(self), )

        self.url =  "../../sites/{}.html".format(uuid.uuid4().int)

    def sensestr(self):
        if len(self.senses) == 0:
            return ""
        else:
            stri = ""
            if Sense.BLINDSIGHT in self.senses:
                stri = "{} blindsight {} ft.,".format(stri, self.senses[Sense.BURROW])
            if Sense.DARKVISION in self.senses:
                stri = "{}, darkvision {} ft.,".format(stri, self.senses[Sense.CLIMB])
            if Sense.TREMORSENSE in self.senses:
                stri = "{}, tremorsense {} ft.,".format(stri, self.senses[Sense.FLY])
            if Sense.TRUESIGHT in self.senses:
                stri = "{}, truesight {} ft.,".format(stri, self.senses[Sense.SWIM])

    def skill(self, sk):
        if sk in self.abilities:
            return self.abilities[sk]
        else:
            if sk._value_ < 1:
                return self.mod(self.abilities.STR)
            elif sk._value_ < 4:
                return self.mod(self.abilities.DEX)
            elif sk._value_ < 9:
                return self.mod(self.abilities.INT)
            elif sk._value_ < 14:
                return self.mod(self.abilities.WIS)
            else:
                return self.mod(self.abilities.CHA)

    def tagstr(self):
        if len(self.tags) == 0:
            return ""
        elif len(self.tags) == 1:
            return "({})".format(self.tags[0])
        else:
            return strself.tags.replace("'","")

    def languagestr(self):
        if len(self.languages) == 0:
            return "-"
        else:
            stri = ""
            for lang in self.languages:
                if lang is self.languages[0]:
                    stri = lang._name_.replace("_", " ").title()
                else:
                    stri = "{}, {}".format(lang._name_.replace("_", " ").title())

            return stri

    def speedstr(self):
        if len(self.speed) == 1:
            return "{} ft.".format(self.speed['speed'])
        else:
            stri = "{} ft.".format(self.speed['speed'])
            if Speed.BURROW in self.speed:
                stri = "{}, burrow {} ft.".format(stri, self.speed[Speed.BURROW])
            if Speed.CLIMB in self.speed:
                stri = "{}, climb {} ft.".format(stri, self.speed[Speed.CLIMB])
            if Speed.FLY in self.speed:
                stri = "{}, fly {} ft.".format(stri, self.speed[Speed.FLY])
            if Speed.SWIM in self.speed:
                stri = "{}, swim {} ft.".format(stri, self.speed[Speed.SWIM])

            return stri

    def mod(self, num):
        return (num - 10) // 2

    def gen_website(self):
        f = open(self.url, 'w')

        body = '''
<html>
<head>
  <title>{}</title>
  <link rel="stylesheet" href="monster.css" />
</head>

<body>
  <div id="wrapper">
    <div id="header">
      <h2>{}</h2>
      <p>{} {} {}, {}</p>
    </div>

    <div id="ac">
      <p><b>Armor Class</b> {}</p>
      <p><b>Hit Points</b> {} ({})</p>
      <p><b>Speed</b> {}</p>
    </div>

    <div id="abilities">
      <div class="ability">
        <div class="top">
          STR
        </div>
        {} ({:+})
      </div>
      <div class="ability">
        <div class="top">
          DEX
        </div>
        {} ({:+})
      </div>
      <div class="ability">
        <div class="top">
          CON
        </div>
        {} ({:+})
      </div>
      <div class="ability">
        <div class="top">
          INT
        </div>
        {} ({:+})
      </div>
      <div class="ability">
        <div class="top">
          WIS
        </div>
        {} ({:+})
      </div>
      <div class="ability">
        <div class="top">
          CHA
        </div>
        {} ({:+})
      </div>
    </div>

    <div id="extras">
      <p><b>Senses</b>{} passive Perception {}</p>
      <p><b>Languages</b> {}</p>
      <p><b>Challenge</b> {}</p>
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

        '''.format(self.name, self.name.upper(), self.size._name_.title(), self.type._name_.lower(), self.tagstr(), self.alignment._name_.replace("_"," ").lower(),
            self.ac, self.hp.avg, self.hp, self.speedstr(), self.abilities.STR, self.mod(self.abilities.STR), self.abilities.DEX, self.mod(self.abilities.DEX),
            self.abilities.CON, self.mod(self.abilities.CON), self.abilities.INT, self.mod(self.abilities.INT), self.abilities.WIS, self.mod(self.abilities.WIS),
            self.abilities.CHA, self.mod(self.abilities.CHA), self.sensestr(), 10 + self.skill(Skill.PERCEPTION), self.languagestr(), self.cr);

        f.write(body)
        f.close()

    def show_website(self):
        if not os.path.exists(self.url):
            self.gen_website()

        webbrowser.open('file://' + os.path.realpath(self.url))

    def __del__(self):
        if os.path.exists(self.url):
            os.remove(self.url)

if __name__ == "__main__":
    Bob = Monster("Commoner")
    Bob.show_website()
    time.sleep(3)
