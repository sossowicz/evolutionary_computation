import numpy as np
import matplotlib.pyplot as plt
import distinctipy

# A class which represents real-valued optimisation problems of different number of dimensions.
class optimisation_problems:
    # Number of dimensions in problem
    def __init__(self, dimensions):
        self.dimensions = dimensions

    # Fitness function implemented in child class
    def fitness(self, position):
        return

# Derived class that implements the Ackley function
class ackley_function(optimisation_problems):
    # Constructor
    def __init__(self, dimensions):
        super().__init__(dimensions)

    # Calculating the fitness as per the Ackley function described in lecture 4
    def fitness(self, position):
        # Compute the two components for readability
        first_term = -20 * np.exp(-0.2 * np.sqrt(np.sum(np.square(position)) / self.dimensions))
        second_term = np.exp(np.sum(np.cos(2 * np.pi * position)) / self.dimensions)
        
        # Combine the components to compute the overall fitness
        fitness_value = first_term - second_term + 20 + np.exp(1)
        
        return fitness_value
    
class standard_pso:
    # Random distribution of particles in swarm
    def create_particle(self):
        index = self.index_counter
        self.index_counter += 1
        position = np.random.uniform(-30, 30, self.problem.dimensions)
        velocity = np.random.uniform(-1, 1, self.problem.dimensions)
        personal_best_score = float('inf')
        personal_best_position = np.zeros(self.problem.dimensions)
        
        return {'index': index, 'position': position, 'velocity': velocity, 'personal_best_score': personal_best_score, 'personal_best_position': personal_best_position}

    # Construct PSO
    def __init__(self, problem, swarm_size=30, w=0.72984, c1=2.05, c2=2.05, max_iter=1000, topology='gbest', wt_min=0.4, wt_max=0.9, n=1, inertia_weight_adjust=False):
        self.problem = problem
        self.swarm_size = swarm_size
        self.w = w
        self.c1 = c1
        self.c2 = c2
        self.max_iter = max_iter
        self.topology = topology
        self.inertia_weight_adjust = inertia_weight_adjust
        self.wt_min = wt_min
        self.wt_max = wt_max
        self.n = n  
        self.index_counter = 0

    def reset(self):
        self.best_fitness_values = []
        self.swcenter_to_globalopt = []
        self.pposition_stddevs = []
        self.velocities_mean = []
               
        self.global_best_score = float('inf')
        self.global_best_position = np.zeros(self.problem.dimensions)
        self.swarm = [self.create_particle() for _ in range(self.swarm_size)]

    def neighbour_topology(self, particle):
        if self.topology == 'gbest':
            return self.global_best_position
        elif self.topology == 'lbest':
            neighbors = [self.swarm[(particle['index'] - 1) % self.swarm_size],
                         self.swarm[(particle['index'] + 1) % self.swarm_size]]
            best_position = min(neighbors, key=lambda x: x['personal_best_score'])['personal_best_position']
            return best_position
        elif self.topology == 'star':
            return self.swarm[0]['personal_best_position']
        elif self.topology == 'random':
            if np.random.random() < 0.5:
                return self.global_best_position
            else:
                neighbors = np.random.choice(self.swarm, size=3, replace=False)
                best_position = min(neighbors, key=lambda x: x['personal_best_score'])['personal_best_position']
                return best_position

    def optimise(self):
        for iteration in range(self.max_iter):
            for i, particle in enumerate(self.swarm):
                fitness = self.problem.fitness(particle['position'])

                # Update personal best score/position
                if fitness < particle['personal_best_score']:
                    particle['personal_best_score'] = fitness
                    particle['personal_best_position'] = particle['position'].copy()

                # Update global best score/position
                if fitness < self.global_best_score:
                    self.global_best_score = fitness
                    self.global_best_position = particle['position'].copy()

            if self.inertia_weight_adjust:
                # Calculate non-linear inertia weight
                t = iteration + 1
                T_max = self.max_iter
                n = 2  # You can adjust this value as needed
                wt_min = 0.4  # You can adjust this value as needed
                wt_max = 0.9  # You can adjust this value as needed
                self.w = ((T_max - t) / T_max) ** n * (wt_min - wt_max) + wt_max

            for particle in self.swarm:
                neighbour_best_position = self.neighbour_topology(particle)

                # Update velocity
                inertia = self.w * particle['velocity']
                cognitive = self.c1 * np.random.random() * (particle['personal_best_position'] - particle['position'])
                social = self.c2 * np.random.random() * (neighbour_best_position - particle['position'])
                particle['velocity'] = inertia + cognitive + social
                
                # Update position
                particle['position'] += particle['velocity']

            self.compute_metrics()
            
            print(f"Iteration {iteration + 1}: Global Best Score = {self.global_best_score}")
        
        self.all_best_fitness_values.append(self.best_fitness_values)
        self.all_swcenter_to_globalopt.append(self.swcenter_to_globalopt)
        self.all_pposition_stddevs.append(self.pposition_stddevs)
        self.all_velocities_mean.append(self.velocities_mean)
                
    def compute_metrics(self):
        # Compute best fitness value
        self.best_fitness_values.append(self.global_best_score)

        # Compute distance of swarm centre to global optimum
        swcenter = np.mean([particle['position'] for particle in self.swarm], axis=0)
        to_globalopt = np.linalg.norm(swcenter)
        self.swcenter_to_globalopt.append(to_globalopt)

        # Compute standard deviation of particle positions
        pposition_stddev = np.std([particle['position'] for particle in self.swarm])
        self.pposition_stddevs.append(pposition_stddev)

        # Compute mean of particle velocities
        v_mean = np.mean([np.linalg.norm(particle['velocity']) for particle in self.swarm])
        self.velocities_mean.append(v_mean)
    
    def run(self, num_runs):
        self.all_best_fitness_values = []
        self.all_swcenter_to_globalopt = []
        self.all_pposition_stddevs = []
        self.all_velocities_mean = []        
        for _ in range(num_runs):   
            self.reset()
            self.optimise()
        self.plot_metrics()  # Corrected method name


    def plot_metrics(self):
        colors = distinctipy.get_colors(len(self.all_best_fitness_values))
        _, fig = plt.subplots(2, 2, figsize=(20, 10))
        fig = fig.flatten()

        for i, color in enumerate(colors):
            fig[0].plot(self.all_best_fitness_values[i], color=color, label=f'Run {i + 1}')
            fig[1].plot(self.all_swcenter_to_globalopt[i], color=color, label=f'Run {i + 1}')
            fig[2].plot(self.all_pposition_stddevs[i], color=color, label=f'Run {i + 1}')
            fig[3].plot(self.all_velocities_mean[i], color=color, label=f'Run {i + 1}')

        fig[0].set_title('Best Fitness')
        fig[0].set_xlabel('Iteration')
        fig[1].set_title('Swcenter to Globalopt')
        fig[1].set_xlabel('Iteration')
        fig[2].set_title('Pposition Stddevs')
        fig[2].set_xlabel('Iteration')
        fig[3].set_title('Velocities Mean')
        fig[3].set_xlabel('Iteration')

        for ax in fig:
            ax.legend()
        
        plt.show()