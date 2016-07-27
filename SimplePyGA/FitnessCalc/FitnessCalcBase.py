class FitnessCalcBase(object):
    """Template class for computing fitness of a given individual vs. a goal or ideal state"""

    # null constructor
    def __init__(self):
        pass

    # simple getFitness example always returns 1.0 (perfect fitness)
    def getFitness(self, indiv, goal):
        return 1.0
