import json
import random

# Loading population
def loadPopulation(fileName):
    with open(fileName, "r") as file:
        population = json.load(file)
    return population

# Generating the initial population
def generatePopulation(popSizes, numCities, numRepetitions):
    for popSize in popSizes:
        for repetitions in range(1, numRepetitions + 1):
            population = []
            for _ in range(popSize):
                individual = list(range(1, numCities + 1))
                random.shuffle(individual)
                population.append(individual)
            fileName = f"out/initial_population/population_{popSize}_rep_{repetitions}.json"
            with open(fileName, "w") as file:
                json.dump(population, file)