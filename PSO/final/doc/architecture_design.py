'''
Basically, we want to Create the functions that can initialized a swarm of points, using EA algorithm to let all point reach point(0,0)

### Core Components:
Optimization_problems Class
·    Used with Ackley_function class, initialized dimensions and fitness functions, it provides the code with flexibility that can support more optimization algorithms.

Ackley_function class
·    Implemented Ackley_function, this function is creates a problem for sets of locations as input, with these locations gradually reach the global center (0,0), the fitness_value will gradually closer to 0, great part about ackley is it can support fitness calculation for location set from multi dimensions.

Standard_pso class
·    This class combined with many functions to support all the optimizing process and plot: init() to initialization, create_particle() to randomly create points of swarms, optimize() + neighbour_topology() as core optimization methods, compute_metrics() + plot_metrics() to plot graph, reset() + run() to run multiple times.

### Task splitting:
We generally have pso_lib.py as a raw code, run.py as testing interface. 

### Testing
Mainly using run.py to test, we will compare different inputs such as: Dimensions of the ackley functions, iterations, swarm size.

'''