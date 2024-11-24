# Simple Random Sampling
import math
import random
import numpy as np

population =  np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

sample_size = 5
sample = np.random.choice(population, size=sample_size, replace=False)

print()
print("Simple Random Sampling in action")
print("Sample: ", sample)

# Systematic Sampling

random_population = np.arange(0, 101)
population_size = len(random_population)

sample_size = 10

# k = N/n. where k - sampling interval, N - population size, n - sample size
k = math.floor(population_size / sample_size)

# Select every k-th element, start from the 0-th element
sample = random_population[::k]

print()
print("Systematic Sampling in action")
print("Sample: ", sample)
