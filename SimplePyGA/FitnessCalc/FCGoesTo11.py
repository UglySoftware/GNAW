import math

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
