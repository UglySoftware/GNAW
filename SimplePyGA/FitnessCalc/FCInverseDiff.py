#-----------------------------------------------------------------------
#
# FCInverseDiff.py
#
#   Fitness calculation using inverse of sum of differences across all
#   genes, comparing an individual to a goal set of genes
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
from . import FitnessCalcBase

class FCInverseDiff(FitnessCalcBase.FitnessCalcBase):

    # computes fitness as inverse of sum of differnces, so that closer matches
    # to the goal get closer to 1.0
    def getFitness(self, indiv, goal):
        try:
            fitnessDelta = [i.absDiff(g) for (i, g) in zip(indiv.genes, goal.genes)]
            return 1.0 / (sum(fitnessDelta) + 1.0)
        except Exception as e:
            print("FCInverseDiff.getFitness() EXCEPTION:", e);
            return 0.0
