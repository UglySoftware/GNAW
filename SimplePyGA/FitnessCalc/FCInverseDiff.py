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
