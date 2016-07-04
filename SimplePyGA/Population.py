# Python library imports
import copy
import random

# SimplePyGA imports
import Gene
import Individual

# Population base class
class Population(object):
    """The population of individuals to evolve using GA"""

    breedingPoolSize = 3

    def __init__(self, popSize, numGenes):
        self.individuals = [Individual.Individual(numGenes) for _ in range(popSize)]

    def size(self):
        return len(self.individuals)

    def mutate(self):
        for i in self.individuals:
            i.mutate()

    def selectForBreeding(self):
        selectedIndices = [random.randrange(0, self.size() - 1) for i in range(Population.breedingPoolSize)]
        return [self.individuals[i] for i in selectedIndices]

    def evolve(self, goal):
        for i in range(self.size()):
            parent1 = getFittest(self.selectForBreeding(), goal)
            parent2 = getFittest(self.selectForBreeding(), goal)
            self.individuals[i] = Individual.breed(parent1, parent2)
        self.mutate()

    def printPop(self, goal):
        for i in self.individuals:
            print i.toString(), ":", getFitness(i, goal)

def getFitness(indiv, goal):
    fitnessDelta = [i.valueDiff(g) for i, g in zip(indiv.genes, goal.genes)]
    return 1.0 / (sum(fitnessDelta) + 1.0)

def getFittest(individuals, goal):
    fittestIndividual = None
    fittestScore = 0
    for i in individuals:
        curFitnessScore = getFitness(i, goal)
        if curFitnessScore > fittestScore:
            fittestIndividual = i
            fittestScore = curFitnessScore
    return fittestIndividual