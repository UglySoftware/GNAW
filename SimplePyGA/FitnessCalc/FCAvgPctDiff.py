from . import FitnessCalcBase

class FCAvgPctDiff(FitnessCalcBase.FitnessCalcBase):

    # computes fitness as the percentage difference between individual and goal
    # on a per-gene basis, compute average percentage, and subtract from 1.0
    # so that closer matches to the goal get closer to 1.0
    def getFitness(self, indiv, goal):
        try:
            fitnessDelta = [i.pctDiff(g) for (i, g) in zip(indiv.genes, goal.genes)]
            return 1.0 - (sum(fitnessDelta) / indiv.numGenes())
        except Exception as e:
            print("FCAvgPctDiff.getFitness() EXCEPTION:", e);
            return 0.0
