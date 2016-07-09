# The Environment is a set of constants that affect the GA and population

# Python library imports
# none

# SimplePyGA imports
import Gene
import Individual
import Population
import FitnessCalc

# GA control settings
promptBetweenGenerations = False
printAllIndividuals = False
printFittestIndividual = True
maxGenerations = 100

# Gene settings
GeneClass = Gene.Gene

# Individual settings
if True:
    IndividualClass = Individual.Individual
    numGenesPerIndividual = 10
    goalIndividualGenes = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]
else:
    IndividualClass = Individual.IndivNamedGenes
    numGenesPerIndividual = 5
    goalIndividualGenes = [7, 100, 8, -41, 1]

# Population settings
PopulationClass = Population.Population
populationSize = 20

# FitnessCalc settings
#FitnessCalcClass = FitnessCalc.FitnessCalc
#FitnessCalcClass = FitnessCalc.FCInverseDiff
#FitnessCalcClass = FitnessCalc.FCAvgPctDiff
FitnessCalcClass = FitnessCalc.FCGoesTo11