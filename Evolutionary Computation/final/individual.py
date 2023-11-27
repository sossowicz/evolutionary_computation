# Represent the individual in the population
class Individual:
    # Initialise individual
    def __init__(self, tsp, tour):
        self.tour = tour
        self.tsp = tsp
        self.fitness = self.calcFitness(tsp)

    # Copy individual
    def copy(self):
        return Individual(self.tsp, self.tour.copy())

    # Calculate fitness of individual 
    def calcFitness(self, tsp):
        totalDistance = 0 # Fitness based on total distance
        for i in range(len(self.tour) - 1):
            totalDistance += tsp.calculateDistance(self.tour[i], self.tour[i+1])
        totalDistance += tsp.calculateDistance(self.tour[-1], self.tour[0])
        return totalDistance