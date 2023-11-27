import random

# Swap Mutation
def swapMutation(individual):
    # Two random positions
    idx1, idx2 = sorted(random.sample(range(len(individual.tour)), 2)) 
    # Swap at chosen positions
    individual.tour[idx1], individual.tour[idx2] = individual.tour[idx2], individual.tour[idx1] 

# Insert Mutation
def insertMutation(individual):
    # Two random positions
    idx1, idx2 = sorted(random.sample(range(len(individual.tour)), 2))
    # Remove the city at idx2 and insert it back at idx1
    city = individual.tour.pop(idx2)
    individual.tour.insert(idx1, city)

# Inversion Mutation
def inversionMutation(individual):
    # Two random positions
    idx1, idx2 = sorted(random.sample(range(len(individual.tour)), 2))
    # Reverse the tour between idx1 and idx2
    individual.tour[idx1:idx2] = reversed(individual.tour[idx1:idx2])