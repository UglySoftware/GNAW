#-----------------------------------------------------------------------
#
# Environment.py
#
#   Settings that define the environment for a Genetic Algorithm (GA)
#   experiment to run in the SimplePyGA framework
#
# Copyright and Distribution
#
#   Part of SimplePyGA: Simple Genetic Algorithms in Python
#   Copyright (c) 2016 Terry McKiernan (terry@mckiernan.com)
#   Released under The MIT License
#   See LICENSE file in top-level package folder
#
#-----------------------------------------------------------------------

# The Environment is a set of constants that affect the GA and population

# Python library imports
#none

# SimplePyGA imports
import Gene
import Individual
import Population
from FitnessCalc import FitnessCalc, FitnessCalcBase, FCAvgPctDiff, FCGoesTo11, FCInverseDiff

# GA control settings
promptBetweenGenerations = False
printAllIndividuals = False
printFittestIndividual = True
maxGenerations = 100
#maxGenerations = -1

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
#FitnessCalcClass = FitnessCalcBase.FitnessCalcBase
#FitnessCalcClass = FCInverseDiff.FCInverseDiff
#FitnessCalcClass = FCAvgPctDiff.FCAvgPctDiff
FitnessCalcClass = FCGoesTo11.FCGoesTo11