import Environment
#import FitnessCalc
import Gene
#import Goal
import Individual
import Population

def printPopulation(pop, generation, goal):
    print "========================================"
    print "GENERATION: ", generation
    print "========================================"
    pop.printPop(goal)
    print "========================================"

# main program
if __name__ == "__main__":
    goal = Environment.IndividualClass(Environment.numGenesPerIndividual, Environment.goalIndividualGenes);
    pop = Environment.PopulationClass(Environment.populationSize, Environment.IndividualClass)
    generation = 0;
    printPopulation(pop, generation, goal)
    #s = raw_input("Press any key...")
    maxFitness = 1.0
    while (maxFitness - Population.getFitness(Population.getFittest(pop.individuals, goal), goal)) > 0.1:
        pop.evolve(goal)
        generation = generation + 1
        printPopulation(pop, generation, goal)
        #s = raw_input("Press any key...")
