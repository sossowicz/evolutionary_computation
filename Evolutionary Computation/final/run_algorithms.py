import json
from genetic_algorithm import GeneticAlgorithm
from inver_over import InverOverAlgorithm
from selection import *
from crossover import *
from mutation import *
from initialisation import loadPopulation

# Save best, median fitness history and best tour to a file
def saveToFile(algorithmName, popSize, rep, bestFitnessHistory, medianFitnessHistory, bestTour):
    # Save best, median fitness history and best tour to a file
    fileName = f"out/best_fitness/{algorithmName}_pop_{popSize}_rep_{rep}.json"
    with open(fileName, "w") as file:
        json.dump(bestFitnessHistory, file)
    fileName = f"out/median_fitness/{algorithmName}_pop_{popSize}_rep_{rep}.json"
    with open(fileName, "w") as file:
        json.dump(medianFitnessHistory, file)
    fileName = f"out/best_tour/{algorithmName}_pop_{popSize}_rep_{rep}.json"
    with open(fileName, "w") as file:
        json.dump(bestTour, file)


# Run algorithms
def runAlgorithms(startRep, endRep, tspInstance):
    # Parameters
    numGenerations = 20000
    popSizes = [20, 50, 100]

    # Define a list of algorithms to test
    algorithms = [
        {
            "name": "Roulette_OX_Swap",
            "selectionMethod": fitnessProportionalSelection,
            "crossoverMethod": orderCrossover,
            "mutationMethod": swapMutation
        },
        {
            "name": "Tournament_PMX_Insert",
            "selectionMethod": tournamentSelection,
            "crossoverMethod": pmxCrossover,
            "mutationMethod": insertMutation
        },
        {
            "name": "Tournament_CX_Inversion",
            "selectionMethod": tournamentSelection,
            "crossoverMethod": cycleCrossover,
            "mutationMethod": inversionMutation
        }
    ]

    # Driver code to Loop through different parameters
    populations = {}
    for rep in range(startRep, endRep + 1):
        # Our Custom Algorithms
        for popSize in popSizes: 
            for algorithm in algorithms: 
                # Load initial population
                fileName = f"out/initial_population/population_{popSize}_rep_{rep}.json"  
                populations[popSize] = loadPopulation(fileName)

                # Create a genetic algorithm instance with chosen parameters
                geneticAlgorithmInstance = GeneticAlgorithm (
                    tspInstance, popSize, numGenerations,
                    initialPopulation = populations[popSize],
                    selectionMethod = algorithm["selectionMethod"],
                    crossoverMethod = algorithm["crossoverMethod"],
                    mutationMethod = algorithm["mutationMethod"]
                )

                # Run algorithm
                bestFitnessHistory, medianFitnessHistory, bestTour = geneticAlgorithmInstance.run()

                # Save best, median fitness history and best tour to a file
                saveToFile(algorithm["name"], popSize, rep, bestFitnessHistory, medianFitnessHistory, bestTour)

        # Inver-Over Algorithm
        popSize = 50

        # Load initial population
        fileName = f"out/initial_population/population_50_rep_{rep}.json"  
        populations[popSize] = loadPopulation(fileName)

        # Create a genetic algorithm instance with chosen parameters
        inverOverAlgorithmInstance = InverOverAlgorithm (
            tspInstance, popSize, numGenerations,
            initialPopulation = populations[popSize]
        )

        # Run algorithm
        bestFitnessHistory, medianFitnessHistory, bestTour = inverOverAlgorithmInstance.run()

        # Save best, median fitness history and best tour to a file
        saveToFile("Inver_Over", popSize, rep, bestFitnessHistory, medianFitnessHistory, bestTour)