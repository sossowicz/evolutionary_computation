import random
import numpy as np
from population import Population

class InverOverAlgorithm:
    def __init__(self, tsp, popSize, numGenerations, initialPopulation):
        self.tsp = tsp
        self.popSize = popSize
        self.numGenerations = numGenerations
        self.initialPopulation = initialPopulation
        self.mutationRate = 0.1
    
    def run(self):
        # Initialise population and lists
        population = Population(self.tsp, self.initialPopulation)
        bestFitnessHistory = []
        medianFitnessHistory = []

        # Run evolution loop
        for gen in range(self.numGenerations):
            print(f"Generation {gen + 1}...")

            for individual in population.individuals:
                new_tour = individual.copy()
                city1 = random.randint(1, len(new_tour.tour))
                idx1 = new_tour.tour.index(city1)

                while True:
                    if (random.random() < self.mutationRate):
                        # select a random city that is different from c
                        city2 = random.randint(1, len(new_tour.tour))
                        while city1 == city2:
                            city2 = random.randint(1, len(new_tour.tour))
                        idx2 = new_tour.tour.index(city2)
                    else:
                        # select a random individual from the population
                        another_tour = random.choice(population.individuals)
                        # find the next city of city1 in another_tour
                        city2 = another_tour.tour[(another_tour.tour.index(city1) + 1) % len(new_tour.tour)]
                        idx2 = new_tour.tour.index(city2)

                    # Terminate if the two cities are adjacent
                    if abs(idx1 - idx2) == 1 or abs(idx1 - idx2) == len(new_tour.tour) - 1:
                        break

                    # Invert the section from the next city of city1 to the city2 in new_tour
                    if idx1 < idx2:
                        new_tour.tour[(idx1 + 1):(idx2 + 1)] = new_tour.tour[(idx1 + 1):(idx2 + 1)][::-1]
                    else:
                        new_tour.tour[idx2:idx1] = new_tour.tour[idx2:idx1][::-1]

                    # Update city1 and idx1
                    city1 = city2
                    idx1 = new_tour.tour.index(city1)

                new_tour.fitness = new_tour.calcFitness(self.tsp)

                # Update individual if new tour is better
                if new_tour.fitness < individual.fitness:
                    individual.tour = new_tour.tour
                    individual.fitness = new_tour.fitness

            # Calculate and store best and median fitness values only if it's the 10th generation or the last generation    
            if (gen + 1) % 10 == 0 or gen == self.numGenerations - 1:
                bestFitness = min(population.individuals, key=lambda x: x.fitness).fitness
                medianFitness = np.median([ind.fitness for ind in population.individuals])
                bestFitnessHistory.append(bestFitness)
                medianFitnessHistory.append(medianFitness)

            bestTour = min(population.individuals, key=lambda x: x.fitness).tour
            
        return bestFitnessHistory, medianFitnessHistory, bestTour