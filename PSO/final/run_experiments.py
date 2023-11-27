from pso_lib import standard_pso, ackley_function

def main():
    dimensions = 10  # You can vary this
    # Define the optimization problem (Ackley function in this case)
    problem = ackley_function(dimensions)
    
    # Create PSO optimiser instance
    swarm_size = 100  # You can vary this
    optimiser = standard_pso(problem=problem, swarm_size=swarm_size, max_iter=1000, topology='gbest', n=2, inertia_weight_adjust=True)
    
    # Run the optimization
    optimiser.run(num_runs=10)
    
if __name__ == '__main__':
    main()
