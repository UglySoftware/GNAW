#-----------------------------------------------------------------------
#
# FCGoesTo11.py
#
#   Fitness calculation checking how close the average of all gene values
#   is to 11.0.  In this case the set of goal genes is not used.
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
import math

# SimplePyGA imports
from . import FitnessCalcBase

class FCGoesTo11(FitnessCalcBase.FitnessCalcBase):

    # computes fitness by taking average of all gene values and seeing how
    # close this is to 11 (ref: This Is Spinal Tap)
    # in this case the "goal" parameter is not used
    def getFitness(self, indiv, goal = None):
        try:
            geneValueAvg = sum([g.getValue() for g in indiv.genes]) / (indiv.numGenes() + 0.0)
            fitnessDelta = math.fabs((geneValueAvg - 11.0) / 137.0)
            return 1.0 - fitnessDelta
        except Exception as e:
            print("FCGoesTo11.getFitness() EXCEPTION:", e);
            return 0.0
