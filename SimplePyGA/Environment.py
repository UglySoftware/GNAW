# The Environment is a set of constants that affect the GA and population

# Python library imports
# none

# SimplePyGA imports
import Individual
import Population

# Individual settings
IndividualClass = Individual.Individual
numGenesPerIndividual = 10
goalIndividualGenes = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]

# Population settings
PopulationClass = Population.Population
populationSize = 20
