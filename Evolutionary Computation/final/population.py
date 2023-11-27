from individual import Individual

class Population:
    def __init__(self, tsp, initialPopulation):
        self.individuals = []
        for i in range(len(initialPopulation)):
            individual = Individual(tsp, initialPopulation[i])
            self.individuals.append(individual)