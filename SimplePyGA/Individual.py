# Python library imports
import copy
import random

# SimplePyGA imports
import Gene

# Constants
NUM_GENES_DEFAULT = 10
CROSSOVER_RATE_DEFAULT = 0.5
GENE_CLASS_DEFAULT = Gene.Gene

# Individual base class
class Individual(object):
    """Individual member of the GA population"""

    crossoverRate = CROSSOVER_RATE_DEFAULT

    def __init__(self, numGenes = NUM_GENES_DEFAULT, geneValues = None, GeneClass = GENE_CLASS_DEFAULT):
        if isinstance(geneValues, list):
            self.genes = [GeneClass("Gene" + str(i), v) for (i, v) in zip(range(len(geneValues)), geneValues)]
        elif isinstance(geneValues, dict):
            self.genes = [GeneClass(k, v) for (k, v) in geneValues.iteritems()]
        else:
            # geneValues is None, or some type we can't process
            self.genes = [GeneClass("Gene" + str(i)) for i in range(numGenes)]

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

class IndivNamedGenes(Individual):
    """Individual member of the GA population"""

    def __init__(self, numGenes = NUM_GENES_DEFAULT, geneValues = None, GeneClass = GENE_CLASS_DEFAULT):
        self.genes = []
        self.genes.append(GeneClass("Foo", valueOrNone(geneValues, 0), 5, 10))
        self.genes.append(GeneClass("Bar", valueOrNone(geneValues, 1), 77, 136))
        self.genes.append(GeneClass("Baz", valueOrNone(geneValues, 2), 1, 9))
        self.genes.append(GeneClass("Waz", valueOrNone(geneValues, 3), -44, -22))
        self.genes.append(GeneClass("Zzz", valueOrNone(geneValues, 4), 0, 1))

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

def valueOrNone(var, index):
    try:
        return var[index]
    except:
        return None

def keyValueOrNone(var, key):
    try:
        return var[key].value
    except:
        return None

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
    i1.setGene(1, Gene.Gene("", 55))
    print "i1 One gene, new value:", i1.getGene(1).getValue()
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    i2 = Individual(10, values)
    print "i2 All genes, initial values:", i2.toString(), "numGenes = ", i2.numGenes()
    i3 = breed(i1, i2)
    print "i3 All genes, initial values:", i3.toString()
    i4 = Individual()
    print "i4, all defaults, initial values:", i4.toString()
    i5 = Individual(3, { "moo" : 3, "boo" : 5, "zoo" : 7 } )
    print "i5, from dictionary, initial values:", i5.toString()
    print i5.genes[1].name
