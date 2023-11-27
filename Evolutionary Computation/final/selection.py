import random

# Roulette wheel
def fitnessProportionalSelection(population):
    # Populations total fitness
    totalFitness = sum(individual.fitness for individual in population.individuals)

    # Selection probabilities of individuals
    probabilities = [1 - (individual.fitness / totalFitness) for individual in population.individuals]
    selectionProbability = [prob / sum(probabilities) for prob in probabilities]

    # Parents selected based on probabilities
    selectedParents = random.choices(population.individuals, selectionProbability, k=len(population.individuals))

    return selectedParents

# Tournament Selection
def tournamentSelection(population):
    tournamentSize = 4
    selectedParents = []
    for _ in range(len(population.individuals)):
        tournamentCandidates = random.sample(population.individuals, tournamentSize)
        selectedParent = min(tournamentCandidates, key=lambda ind: ind.fitness)
        selectedParents.append(selectedParent)
            
    return selectedParents 