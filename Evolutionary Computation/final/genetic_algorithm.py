import random
import numpy as np
from population import Population

class GeneticAlgorithm:
    def __init__(self, tsp, popSize, numGenerations,
                 initialPopulation, selectionMethod, crossoverMethod, mutationMethod):
        self.tsp = tsp
        self.popSize = popSize
        self.numGenerations = numGenerations
        self.initialPopulation = initialPopulation
        self.selectionMethod = selectionMethod
        self.crossoverMethod = crossoverMethod
        self.mutationMethod = mutationMethod
        self.mutationRate = 0.05
        self.elitismRate = 0.1
    
    def run(self):
        # Initialise population and lists
        population = Population(self.tsp, self.initialPopulation)
        bestFitnessHistory = []
        medianFitnessHistory = []

        # Run evolution loop
        for gen in range(self.numGenerations):
            print(f"Generation {gen + 1}...")

            # Selection
            selectedParents = self.selectionMethod(population)

            # Crossover
            children = []
            for i in range(0, len(selectedParents), 2):
                parent1 = selectedParents[i]
                if i + 1 < len(selectedParents):
                    parent2 = selectedParents[i + 1]
                else:
                    parent2 = selectedParents[0]
                child1, child2 = self.crossoverMethod(parent1, parent2)
                children.append(child1)
                children.append(child2)

            # Mutation
            for child in children:
                if random.random() < self.mutationRate:
                    self.mutationMethod(child)

            # Calculate and store best and median fitness values only if it's the 10th generation or the last generation
            if (gen + 1) % 10 == 0 or gen == self.numGenerations - 1:
                bestFitness = min(population.individuals, key=lambda x: x.fitness).fitness
                medianFitness = np.median([ind.fitness for ind in population.individuals])
                bestFitnessHistory.append(bestFitness)
                medianFitnessHistory.append(medianFitness)

            # Elitism 
            eliteNum = int(self.elitismRate * self.popSize)
            sorted_individuals = sorted(population.individuals, key=lambda x: x.fitness)
            elite_individuals = sorted_individuals[:eliteNum]
            
            # Replacement - Replace the entire previous generation with the new generation
            new_population = elite_individuals + children[:self.popSize - eliteNum]
            population.individuals = new_population
        
        bestTour = min(population.individuals, key=lambda x: x.fitness).tour

        return bestFitnessHistory, medianFitnessHistory, bestTour