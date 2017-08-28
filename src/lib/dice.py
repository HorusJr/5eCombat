import math, random

class Dice:
    def __init__(self, number, sides):
        self.number = number
        self.sides = sides
        self.avg = math.floor(number * sides/2)

    def roll(self):
        rolls = []
        for i in range(number):
            rolls.append(random.randint(1, sides))

        return (sum(rolls), rolls)

    def __str__(self):
        return "{0}d{1}".format(self.number, self.sides)
