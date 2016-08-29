#-----------------------------------------------------------------------
#
# FCNumPyExample.py
#
#   Fitness calculation demonstrating use of NumPy.  This shows how
#   you can extend the overall SimplePyGA system to bring in external
#   scientific libraries etc.
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
import numpy as np

# SimplePyGA imports
from . import FitnessCalcBase

class FCNumPyExample2(FitnessCalcBase.FitnessCalcBase):

    # Another simple NumPy example
    # Load indiv genes and goal into NumPy arrays
    # Computes vector magnitude (sqrt(vec elements squared))
    # Closer to goal magnitude = higher fitness
    def getFitness(self, indiv, goal):
        try:
            i = np.array([_.value for _ in indiv.genes])
            iMag = math.sqrt(np.sum(i * i))
            g = np.array([_.value for _ in goal.genes])
            gMag = math.sqrt(np.sum(g * g))
            dp = math.fabs(iMag - gMag)
            fitness = 1.0 / (dp + 1.0)
        except Exception as e:
            print("FCNumPyExample.getFitness() EXCEPTION:", e);
            fitness = 0.0
        return fitness
