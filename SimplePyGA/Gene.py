#-----------------------------------------------------------------------
#
# Gene.py
#
#   Gene class for SimplePyGA
#
# Copyright and Distribution
#
#   Part of SimplePyGA: Simple Genetic Algorithms in Python
#   Copyright (c) 2016 Terry McKiernan (terry@mckiernan.com)
#   Released under The MIT License
#   See LICENSE file in top-level package folder
#
#-----------------------------------------------------------------------

# Python library imports
import math
import random

# SimplePyGA imports
#none

# Gene base class
class Gene(object):
    """A single gene of a GA Individual"""

    minValue = 0
    maxValue = 100
    mutationRate = 0.02

    def __init__(self, name = "", value = None, minValue = None, maxValue = None):
        self.name = name
        if minValue is not None: self.minValue = minValue
        if maxValue is not None: self.maxValue = maxValue
        if value is None:
            self.value = self.__randomValue()
        else:
            self.value = value

    def getValue(self):
        return self.value

    # set gene value
    # TODO: check if new value is within bounds; if not raise range error exception
    def setValue(self, value):
        self.value = value

    def __randomValue(self):
        return random.randint(self.minValue, self.maxValue)

    def absDiff(self, other):
        return math.fabs(self.getValue() - other.getValue())

    def pctDiff(self, other):
        return self.absDiff(other) / (self.maxValue - self.minValue + 1)

    def mutate(self):
        if random.random() <= Gene.mutationRate:
            self.value = self.__randomValue()

if __name__ == "__main__":
    g1 = Gene("g1", 10)
    print("Gene initial value:", g1.getValue())
    Gene.mutationRate = 1.0
    g1.mutate()
    print("Gene value after mutation:", g1.getValue())
    g1.setValue(99)
    print("Gene new value:", g1.getValue())
    print("g1.minValue", g1.minValue)
    print("g1.maxValue", g1.maxValue)
    g2 = Gene("g2", 20)
    print("g2.minValue", g2.minValue)
    print("g2.maxValue", g2.maxValue)
    g2.minValue = 3
    g2.maxValue = 77
    print("g2.minValue", g2.minValue)
    print("g2.maxValue", g2.maxValue)
    print("g1.minValue", g1.minValue)
    print("g1.maxValue", g1.maxValue)
    g3 = Gene()
    print("g3.minValue", g3.minValue)
    print("g3.maxValue", g3.maxValue)
