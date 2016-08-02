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

class FCNumPyExample(FitnessCalcBase.FitnessCalcBase):

    # Very simply NumPy example
    # Load indiv genes and goal into NumPy arrays
    # Takes dot product
    # Zero = perfect fitness
    def getFitness(self, indiv, goal):
        try:
            i = np.array([_.value for _ in indiv.genes])
            g = np.array([_.value for _ in goal.genes])
            dp = math.fabs(i.dot(g))
            fitness = 1.0 / (dp + 1.0)
        except Exception as e:
            print("FCNumPyExample.getFitness() EXCEPTION:", e);
            fitness = 0.0
        return fitness
