# Python library imports
import copy
import random

# SimplePyGA imports
import Gene

# Constants
NUM_GENES_DEFAULT = 10
CROSSOVER_RATE_DEFAULT = 0.5

# Individual base class
class Individual(object):
    """Individual member of the GA population"""

    def __init__(self, numGenes = NUM_GENES_DEFAULT, geneValues = None, crossoverRate = CROSSOVER_RATE_DEFAULT):
        self.crossoverRate = crossoverRate
        if geneValues is None:
            self.genes = [Gene.Gene() for i in range(numGenes)]
        else:
            self.genes = [Gene.Gene(v) for v in geneValues]

    def getGene(self, keyOrIndex):
        return self.genes[keyOrIndex]

    def setGene(self, keyOrIndex, gene):
        self.genes[keyOrIndex] = gene

    def numGenes(self):
        return len(self.genes)

    def mutate(self):
        for g in self.genes:
            g.mutate()

    def toString(self):
        return " ".join([str(g.getValue()) for g in self.genes])

def breed(parent1, parent2):
    child = copy.deepcopy(parent1)
    for (cg, pg2) in zip(child.genes, parent2.genes):
        if random.random() <= child.crossoverRate:
            cg = copy.deepcopy(pg2)
    return child

if __name__ == "__main__":
    i1 = Individual(10)
    print "i1 All genes, initial values:", i1.toString()
    Gene.Gene.mutationRate = 0.5
    i1.mutate()
    print "i1 All genes, after mutation:", i1.toString()
    print "i1 One gene, initial value:", i1.getGene(1).getValue()
    i1.setGene(1, Gene.Gene(55))
    print "i1 One gene, new value:", i1.getGene(1).getValue()
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    i2 = Individual(10, values)
    print "i2 All genes, initial values:", i2.toString(), "numGenes = ", i2.numGenes()
    i3 = breed(i1, i2)
    print "i3 All genes, initial values:", i3.toString()
    I4 = Individual()
    print "i4, all defaults, initial values:", I4.toString()