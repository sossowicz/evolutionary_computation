import numpy as np

class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Load TSP data
class TSP:
    def __init__(self, filePath):
        self.filePath = filePath
        self.cities = []
        self.parseFile()
        
    # Parse TSP data for city co-ords
    def parseFile(self):
        with open(self.filePath, "r") as file:
            for line in file:
                if line.startswith("NODE_COORD_SECTION"):
                    break
            for line in file:
                if line.strip() == "EOF":
                    break
                parts = line.split()
                x = float(parts[1])
                y = float(parts[2])
                self.cities.append(City(x, y))  # Create City objects

    def calculateDistance(self, city1, city2):
        x1, y1 = self.cities[city1 - 1].x, self.cities[city1 - 1].y
        x2, y2 = self.cities[city2 - 1].x, self.cities[city2 - 1].y
        return np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Extract optimal tour from file
def optimalTour(fileName):
    optimalTourOrder = []
    with open(fileName, "r") as file:
        lines = file.readlines()
        readTour = False
        for line in lines:
            if readTour:
                if line.strip() == "-1":
                    break
                cityID = int(line.strip())
                optimalTourOrder.append(cityID)
            elif line.strip() == "TOUR_SECTION":
                readTour = True
    return optimalTourOrder