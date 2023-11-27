from tsp import TSP
from initialisation import generatePopulation
from run_algorithms import runAlgorithms
from diagram import *

# Create TSP instance
tspInstance = TSP("tsp/pcb442.tsp")

# Parameters
popSizes = [20, 50, 100]
numRepetitions = 30

# Generate initial population
generatePopulation(popSizes, len(tspInstance.cities), numRepetitions)

# Run algorithms
startRep = 1
endRep = 30
runAlgorithms(startRep, endRep, tspInstance)

# Generate diagrams
generateDiagrams(tspInstance, numRepetitions)