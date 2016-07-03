import random
import math

class Individual:
    """Individual member of the GA population"""

    crossoverRate = 0.5
    mutationRate = 0.015

    minGeneVal = 1
    maxGeneVal = 100
    numGenesDefault = 10

    def __init__(self, genes = None):
        if genes is None:
            self.genes  = generateRandomGenes()
        else:
            self.genes = genes

    def numGenes(self):
        return len(self.genes)

    def getGene(self, index):
        return self.genes[index]

    def setGene(self, index, value):
        self.genes[index] = value

    def mutate(self):
        #print "Mutate BEFORE:", self.genes
        for i in range(self.numGenes()):
            if random.random() <= Individual.mutationRate:
                self.setGene(i, randomGene())
        #print "Mutate AFTER:", self.genes

    def toString(self):
        return "".join([str(_) for _ in self.genes])

class Population:
    """The population of individuals to evolve using GA"""

    popSizeDefault = 10
    tournamentSize = 3

    def __init__(self, popSize):
        self.individuals = [Individual() for _ in range(popSize)]

    def size(self):
        return len(self.individuals)

    def mutate(self):
        for i in self.individuals:
            i.mutate()

    def selectForTournament(self):
        selectedIndices = [random.randrange(0, self.size() - 1) for i in range(Population.tournamentSize)]
        return [self.individuals[i] for i in selectedIndices]

    def evolve(self, goal):
        for i in range(self.size()):
            i1 = getFittest(self.selectForTournament(), goal)
            i2 = getFittest(self.selectForTournament(), goal)
            self.individuals[i] = crossover(i1, i2)
        self.mutate()

    def printPop(self, goal):
        for i in self.individuals:
            print i.genes, getFitness(i, goal)

def crossover(parent1, parent2):
    child = Individual()
    for i in range(parent1.numGenes()):
        if random.random() <= Individual.crossoverRate:
            child.setGene(i, parent1.getGene(i))      
        else:
            child.setGene(i, parent2.getGene(i))      
    return child

def getFitness(indiv, goal):
    fitnessDelta = [math.fabs(i - g) for i, g in zip(indiv.genes, goal)]
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

def randomGene(minGeneVal = Individual.minGeneVal, maxGeneVal = Individual.maxGeneVal):
    return random.randint(minGeneVal, maxGeneVal)

def generateRandomGenes(numGenes = Individual.numGenesDefault, minGeneVal = Individual.minGeneVal, maxGeneVal = Individual.maxGeneVal):
    return [randomGene(minGeneVal, maxGeneVal) for _ in range(numGenes)]

def printPopulation(pop, generation, goal):
    print "========================================"
    print "GENERATION: ", generation
    print "========================================"
    pop.printPop(goal)
    print "========================================"

# main program
if __name__ == "__main__":
    goal = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95];
    maxFitness = 1.0
    pop = Population(20)
    generation = 0;
    printPopulation(pop, generation, goal)
    s = raw_input("Press any key...")
    while (maxFitness - getFitness(getFittest(pop.individuals, goal), goal)) > 0.1:
        pop.evolve(goal)
        generation = generation + 1
        printPopulation(pop, generation, goal)
        #s = raw_input("Press any key...")
