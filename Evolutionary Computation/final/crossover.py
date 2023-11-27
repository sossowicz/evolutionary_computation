import random
from individual import Individual

# Order Crossover
def orderCrossover(parent1, parent2):
    size = len(parent1.tour)
    child1, child2 = [-1] * size, [-1] * size # Placeholder
    start, end = sorted([random.randrange(size) for _ in range(2)])
    
    # Choose an arbitrary part from the first parent (and the second parent for the second child)
    # Copy this part to the first child (and to the second child from the second parent)
    for i in range(start, end + 1):
        child1[i] = parent1.tour[i]
        child2[i] = parent2.tour[i]

    # Copy the numbers that are not in the first part, to the first child, analygous for the second child, with parent roles reversed
    idx1 = (end + 1) % size
    idx2 = (end + 1) % size
    for i in range(size):
        if parent2.tour[i] not in child1:
            child1[idx1] = parent2.tour[i]
            idx1 = (idx1 + 1) % size
        
        if parent1.tour[i] not in child2:
            child2[idx2] = parent1.tour[i]
            idx2 = (idx2 + 1) % size
    
    return Individual(parent1.tsp, child1), Individual(parent1.tsp, child2)

# Partially Mapped Crossover
def pmxCrossover(parent1, parent2):
    size = len(parent1.tour)
    child1, child2 = [-1] * size, [-1] * size # Placeholder

    # Choose random segment and copy it from P1
    start, end = sorted([random.randrange(size) for _ in range(2)])
    for i in range(start, end + 1):
        child1[i] = parent1.tour[i]
        child2[i] = parent2.tour[i]

    for i in range(size):
        if start <= i <= end:
            continue

        value = parent1.tour[i]
        while value in child1[start:end + 1]:
            idx = parent1.tour.index(value)
            value = parent1.tour[idx]
        child1[i] = value

        value = parent2.tour[i]
        while value in child2[start:end + 1]:
            idx = parent2.tour.index(value)
            value = parent2.tour[idx]
        child2[i] = value
    
    return Individual(parent1.tsp, child1), Individual(parent1.tsp, child2)

# Cycle Crossover
def cycleCrossover(parent1, parent2):
    size = len(parent1.tour)
    child1, child2 = [-1] * size, [-1] * size # Placeholder   

    # First cycle
    idx = 0
    while child1[idx] == -1:
        child1[idx] = parent1.tour[idx]
        idx = parent1.tour.index(parent2.tour[idx])

    # Fill positions with values from the other parent
    for i in range(size):
        if child1[i] == -1:
            child1[i] = parent1.tour[i]
        if child2[i] == -1:
            child2[i] = parent2.tour[i]
    
    return Individual(parent1.tsp, child1), Individual(parent1.tsp, child2)