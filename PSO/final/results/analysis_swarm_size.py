'''
How variable are the runs for different swarm sizes?
A metric plot of population size of 20 shows relatively high variability between runs. Some runs converge quickly,others require more iterations to converge. The smaller group sizes can lead to more exploratory searches.

Population size of 100: Indicators with a population size of 100 exhibit less variability than those with a population size of 20. Running tends to converge faster and more consistently. The larger group size allows for faster convergence.

Population size 200: When the population size is 200, the indicator plot shows less variability. Most runs converge quickly and follow a similar convergence path. Larger group sizes allow better coverage of the solution space and facilitate faster convergence.

How many iterations are needed to converge approximately / Which swarm size converges faster? 
From reading the Best fitness graph, we can conclude that;
Smaller population sizes (20) appear to converge very randomly, between 20-400 iterations.
Medium-size clusters (100) converge slower but more consistently, between a range of 50-150 at latest.
Larger population sizes (200) converge the fastest, with many runs converging within 20-150 iterations because they can efficiently explore and utilize the search space.

Which swarm size gets closer to the global optimum? 
We see in the diagrams that both populations 100 and 200 reach the global minimum, where the population of 20 gets close but will not reach it.

How might those differences be caused by the swarm size?
The differences in convergence rate and degree of approximation to global optimum are mainly caused by population size. Larger group sizes allow for more comprehensive exploration, faster convergence and a better chance of discovering optimal solutions. 

Which swarm size would you choose?
Best group size depends on the balance between computational resources and optimization performance. Population size of 100 strikes a good balance, providing fast convergence and near global optimality. However, if the computing resources are not limited, we would choose a group size of 200 consistent solution quality.
'''