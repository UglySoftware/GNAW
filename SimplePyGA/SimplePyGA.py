#-----------------------------------------------------------------------
#
# SimplePyGA.py
#
#   Main program for SimplePyGA
#
#   Executes a Genetic Algorithm (GA) for a population, using parameters
#   specified in Environment.py
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
#none

# SimplePyGA imports
import Environment
import FitnessCalc
import Gene
import Individual
import Population

def printPopulation(pop, generation, goal):
    print("========================================")
    print("GENERATION: ", generation)
    print("========================================")
    pop.printPop(goal)
    print("========================================")

def printFittest(generation, fittestIndividual, fittestScore):
    print("Generation", generation, "Fittest Individual:", fittestIndividual.toString(), "Score:", fittestScore)

# main program
if __name__ == "__main__":
    goal = Environment.IndividualClass(Environment.numGenesPerIndividual, Environment.goalIndividualGenes);
    fitnessCalc = Environment.FitnessCalcClass()
    pop = Environment.PopulationClass(Environment.populationSize, Environment.IndividualClass, fitnessCalc)
    generation = 0;
    while True:
        if Environment.printAllIndividuals:
            printPopulation(pop, generation, goal)
        fittestIndividual = FitnessCalc.FitnessCalc.getFittest(pop.individuals, goal, fitnessCalc)
        fittestScore = fitnessCalc.getFitness(fittestIndividual, goal)
        if Environment.printFittestIndividual:
            printFittest(generation, fittestIndividual, fittestScore)
        if (fittestScore != 1.0) and ((Environment.maxGenerations < 0) or (Environment.maxGenerations > generation)):
            if Environment.promptBetweenGenerations:
                s = raw_input("Press Enter to proceed to next generation...")
            pop.evolve(goal)
            generation = generation + 1
        else:
            break
    print("DONE!")
    print("Number of generations:", generation)
    printFittest(generation, fittestIndividual, fittestScore)
