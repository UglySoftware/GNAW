def getFittest(individuals, goal, fitnessCalc):
    fittestIndividual = None
    fittestScore = 0
    for i in individuals:
        curFitnessScore = fitnessCalc.getFitness(i, goal)
        if (fittestIndividual is None) or (curFitnessScore > fittestScore):
            fittestIndividual = i
            fittestScore = curFitnessScore
    return fittestIndividual