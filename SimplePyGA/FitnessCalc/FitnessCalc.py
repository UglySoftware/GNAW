#-----------------------------------------------------------------------
#
# FitnessCalc.py
#
#   Utility functions for fitness calculations in SimplePyGA
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
#none

def getFittest(individuals, goal, fitnessCalc):
    fittestIndividual = None
    fittestScore = 0
    for i in individuals:
        curFitnessScore = fitnessCalc.getFitness(i, goal)
        if (fittestIndividual is None) or (curFitnessScore > fittestScore):
            fittestIndividual = i
            fittestScore = curFitnessScore
    return fittestIndividual