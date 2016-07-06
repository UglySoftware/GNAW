# Python library imports
import math
import random

# Gene base class
class Gene(object):
    """A single gene of a GA Individual"""

    minValue = 0
    maxValue = 100
    mutationRate = 0.02

    def __init__(self, value = None):
        if value is None:
            self.value = self.randomValue()
        else:
            self.value = value

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

    def randomValue(self):
        return random.randint(Gene.minValue, Gene.maxValue)

    def absDiff(self, other):
        return math.fabs(self.getValue() - other.getValue())

    def pctDiff(self, other):
        return self.absDiff(other) / (self.maxValue - self.minValue + 1)

    def mutate(self):
        if random.random() <= Gene.mutationRate:
            self.value = self.randomValue()

# NumericGene is really just the same as the base class Gene
class NumericGene(Gene):
    """A gene that holds a numeric value"""

if __name__ == "__main__":
    g1 = Gene(10)
    print "Gene initial value:", g1.getValue()
    Gene.mutationRate = 1.0
    g1.mutate()
    print "Gene value after mutation:", g1.getValue()
    g1.setValue(99)
    print "Gene new value:", g1.getValue()
    print g1.minValue
    print g1.maxValue
