# Pythong library imports
import math

# SimplePyGA imports
import Gene
import Individual
import Population

class FitnessCalc(object):
    """Template class for computing fitness of a given individual vs. a goal or ideal state"""

    # null constructor
    def __init__(self):
        pass

    # simple getFitness example always returns 1.0 (perfect fitness)
    def getFitness(self, indiv, goal):
        return 1.0

class FCInverseDiff(FitnessCalc):

    # computes fitness as inverse of sum of differnces, so that closer matches
    # to the goal get closer to 1.0
    def getFitness(self, indiv, goal):
        try:
            fitnessDelta = [i.absDiff(g) for (i, g) in zip(indiv.genes, goal.genes)]
            return 1.0 / (sum(fitnessDelta) + 1.0)
        except Exception as e:
            print("FCInverseDiff.getFitness() EXCEPTION:", e);
            return 0.0

class FCAvgPctDiff(FitnessCalc):

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

class FCGoesTo11(FitnessCalc):

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

def getFittest(individuals, goal, fitnessCalc):
    fittestIndividual = None
    fittestScore = 0
    for i in individuals:
        curFitnessScore = fitnessCalc.getFitness(i, goal)
        if (fittestIndividual is None) or (curFitnessScore > fittestScore):
            fittestIndividual = i
            fittestScore = curFitnessScore
    return fittestIndividual