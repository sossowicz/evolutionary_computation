'''
# Overall Comparison:

Fully Connected Swarm (gbest): This topology often produced the best results in terms of convergence speed and final fitness. It promotes global exploration by allowing all particles to communicate with each other.

Ring Topology (lbest): This topology showed balanced performance. It enables limited local exploration by allowing each particle to communicate with its immediate neighbors. It strikes a balance between exploration and exploitation.

Star Topology: The star topology did not perform as well as gbest or lbest. It promotes centralized exploration, which led to a slower convergence speed and potentially getting stuck in local optima.

Random 50% Neighborhood: The random neighborhood was the most diverse but exhibited slower convergence and inconsistent results. The randomness can hinder convergence by limiting the influence of better-performing neighbors.

# Swarm Behavior:

Fully connected swarms (gbest) were the most cohesive, leading to narrower swarm distributions. Particles often moved in harmony towards a global optimum.

Ring topology (lbest) produced a more distributed swarm as each particle only considers a few neighbors, resulting in a slightly wider swarm distribution.

Star topology had a more centralized swarm, often resulting in a narrow swarm distribution with particles focused around a local optimum.

Random neighborhoods created highly distributed swarms with widely varying distributions, leading to the widest swarm behavior.

# Convergence Speed:

Fully connected swarms (gbest) converged the fastest due to global information sharing, followed by ring topology, star topology, and random neighborhoods, which had the slowest convergence.

# Performance and Speed:

Fully connected swarms performed the fastest due to efficient global information sharing.

Star topology, although slow, was faster than the random neighborhood due to its deterministic nature.

# Final Results:

Fully connected (gbest) produced the best results in terms of final fitness.

Ring topology (lbest) showed good convergence and moderate final fitness.

Star topology led to slower convergence and lower final fitness.

Random neighborhoods had inconsistent results and slower convergence.
'''