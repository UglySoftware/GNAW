#-----------------------------------------------------------------------
#
# FitnessCalcBase.py
#
#   Base class for fitness calculations. Always returns 1.0 (perfect).
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

class FitnessCalcBase(object):
    """Template class for computing fitness of a given individual vs. a goal or ideal state"""

    # null constructor
    def __init__(self):
        pass

    # simple getFitness example always returns 1.0 (perfect fitness)
    def getFitness(self, indiv, goal):
        return 1.0
