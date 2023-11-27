import matplotlib.pyplot as plt
import json
from individual import Individual
from tsp import *

# Load the best or median fitness history
def loadFitnessHistory(algorithm, popSize, rep, best = True):
    if best:
        fileName = f"out/best_fitness/{algorithm}_pop_{popSize}_rep_{rep}.json"
    else:
        fileName = f"out/median_fitness/{algorithm}_pop_{popSize}_rep_{rep}.json"
    with open(fileName, "r") as file:
        fitnessHistory = json.load(file)
    return fitnessHistory

# Load the best tour for a given algorithm
def loadBestTour(numRepetitions, algorithm):
    popSize = 100
    if algorithm == "Inver_Over":
        popSize = 50

    # Find the best repetition
    for rep in range(1, numRepetitions + 1):
        bestFitnessHistory = loadFitnessHistory(algorithm, popSize, rep, best = True)
        if rep == 1:
            bestFitness = bestFitnessHistory[-1]
            bestRep = rep
        elif bestFitnessHistory[-1] < bestFitness:
            bestFitness = bestFitnessHistory[-1]
            bestRep = rep

    # Load the best tour
    fileName = f"out/best_tour/{algorithm}_pop_{popSize}_rep_{bestRep}.json"
    with open(fileName, "r") as file:
        bestTour = json.load(file)
    return bestTour
    
# Create a plot to compare the best fitness and median fitness of different algorithms
def createPlot(pop, rep, algorithms):
    # Define generations
    generations = range(10, 20001, 10)

    # Create a subplot
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111)
    fig.subplots_adjust(left=0.15)

    # Plot the data
    i = 0

    for algorithm in algorithms:
        if algorithm == "Inver_Over":
            continue
        i += 1
        bestFitnessHistory = loadFitnessHistory(algorithm, pop, rep, best = True)
        medianFitnessHistory = loadFitnessHistory(algorithm, pop, rep, best = False)
        ax.plot(generations, bestFitnessHistory, label = f"Algorithm {i} - Best Fitness", marker = "x", markevery = (50, 100), markersize = 10)
        if (i == 3):
            ax.plot(generations, medianFitnessHistory, label = f"Algorithm {i} - Median Fitness", color = "teal")
        else:
            ax.plot(generations, medianFitnessHistory, label = f"Algorithm {i} - Median Fitness")
    
    # Set labels and title
    ax.set_xlabel('Generation')
    ax.set_ylabel('Fitness')
    ax.set_title(f"Population Size: {pop}, Repetition: {rep}")
    ax.legend()
    
    # Save the plot
    formatted_rep = str(rep).zfill(2)
    fileName = f"results/repetition{formatted_rep}_pop{pop}.png"
    plt.savefig(fileName)
    plt.close()

# Create a boxplot to compare the best fitness across different algorithms
def createBoxPlot(numRepetitions, algorithms):
    # Define parameters 
    bestFitnesses = {}
    for algorithm in algorithms:
        bestFitnesses[algorithm] = []

    # Load best fitnesses
    for rep in range(1, numRepetitions + 1):
        for algorithm in bestFitnesses:
            if algorithm == "Inver_Over":
                bestFitnessHistory = loadFitnessHistory(algorithm, 50, rep, best = True)
            else:
                bestFitnessHistory = loadFitnessHistory(algorithm, 100, rep, best = True)
            bestFitnesses[algorithm].append(bestFitnessHistory[-1])    

    # Create a figure and axis
    fig = plt.figure(figsize=(8, 12))
    ax = fig.add_subplot(111)
    ax.boxplot(bestFitnesses.values())
    ax.set_xticklabels(["Algorithm 1", "Algorithm 2", "Algorithm 3", "Inver-Over"])
    ax.set_ylabel('Fitness')
    ax.set_title(f"Best Fitness across Algorithms")
    fig.subplots_adjust(left=0.15)

    # Make the lowest fitness of best fitness of each algorithm appear as red dots
    i = 0
    for algorithm in bestFitnesses:
        i += 1
        bestFitness = min(bestFitnesses[algorithm])
        ax.plot(i, bestFitness, marker = "o", c = "red", markersize = 5)
        ax.annotate(f"{bestFitness:.2f}", (i, bestFitness), xytext = (i + 0.1, bestFitness - 3000))
    
    # Save the plot
    fileName = f"results/algorithm_stats.png"
    plt.savefig(fileName)
    plt.close()

# Create a plot to display the best tour for each algorithm and the optimal tour
def createTourPlot(numRepetitions, tspInstance, algorithms):
    # Load the optimal tour
    tourFile = "tsp/pcb442.opt.tour"
    optimal = Individual(tspInstance, optimalTour(tourFile))
    tours = ["Optimal Tour"] + algorithms

    # Create a plot
    fig = plt.figure(figsize=(16, 16))
    ax = fig.add_subplot(111)
    fig.subplots_adjust(left=0.15)

    # Set cities in the plot to red dots
    x = []
    y = []
    for city in tspInstance.cities:
        x.append(city.x)
        y.append(city.y)
    ax.scatter(x, y, c = "black", s = 15)

    # Plot the best tour for each algorithm in the same plot
    i = -1
    for tour in tours:
        if tour == "Inver_Over":
            continue

        i += 1
        if tour == "Optimal Tour":
            bestTour = optimal.tour
        else:
            bestTour = loadBestTour(numRepetitions, tour)

        x = []
        y = []
        for city in bestTour:
            x.append(tspInstance.cities[city - 1].x)
            y.append(tspInstance.cities[city - 1].y)
        if tour == "Optimal Tour":
            ax.plot(x, y, label = f"{tour}", c = "red")
        else:
            ax.plot(x, y, label = f"Algorithm {i}")

    # Set labels and title
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title('Best Tour')
    ax.legend()

    # Save the plot
    fileName = f"results/algorithm_solution.png"
    plt.savefig(fileName)
    plt.close()

    # Plot the best tour for each algorithm in a separate plot
    i = 0
    for tour in tours:
        if tour == "Optimal Tour":
            continue

        i += 1
        fig = plt.figure(figsize=(16, 16))
        ax = fig.add_subplot(111)

        # Set cities in the plot to red dots
        x = []
        y = []

        for city in tspInstance.cities:
            x.append(city.x)
            y.append(city.y)
        ax.scatter(x, y, c = "black", s = 15)

        # Plot the best tour for each algorithm in the same plot
        x = []
        y = []
        for city in optimal.tour:
            x.append(tspInstance.cities[city - 1].x)
            y.append(tspInstance.cities[city - 1].y)
        ax.plot(x, y, label = f"Optimal Tour", c = "red")
        
        x = []
        y = []

        bestTour = loadBestTour(numRepetitions, tour)
        for city in bestTour:
            x.append(tspInstance.cities[city - 1].x)
            y.append(tspInstance.cities[city - 1].y)
        
        if tour == "Inver_Over":
            tourLabel = "Inver_Over"
        else:
            tourLabel = f"Algorithm_{i}"
        
        ax.plot(x, y, label = f"{tourLabel}")
        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')
        ax.set_title(f"Best Tour - {tour}")
        ax.legend()
    
        # Save the plot
        fileName = f"results/algorithm_solution_{tourLabel}.png"
        plt.savefig(fileName)
        plt.close()


# Main function
def generateDiagrams(tspInstance, numRepetitions):
    popSizes = [20, 50, 100]
    algorithms = ["Roulette_OX_Swap", "Tournament_PMX_Insert", "Tournament_CX_Inversion", "Inver_Over"]

    # Create a plot to compare the best fitness and median fitness of different algorithms
    for pop in popSizes:
        for rep in range(1, numRepetitions + 1):
            createPlot(pop, rep, algorithms)

    # Create a boxplot to compare the best fitness across different algorithms
    createBoxPlot(numRepetitions, algorithms)

    # Create a plot to display the best tour
    createTourPlot(numRepetitions, tspInstance, algorithms)