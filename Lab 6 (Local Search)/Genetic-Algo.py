# Solving N-Queens Using Genetic Algorithm:
# Step 1: Define the Problem and Fitness Function
# Create a fitness function that counts the number of non-attacking pairs of queens.
# ● A higher fitness score means fewer conflicts (non-attacking pairs).
# ● Each queen must be placed in a different column, so the chromosome is a list of column positions for each row.

# Step 2: Initialize the Population
# This function generates a random route (a chromosome) by:
# ● Creating a list of indices representing the unique column position of each queen in a row (e.g., [3, 0, 2, 1]).
# ● This creates an initial population of 10 random boards.
# ● Each board state is a potential solution, and the population is a collection of these solutions

# Step 3: Evaluate Fitness
# ● Evaluates the fitness of each board state based on non-attacking pairs.
# ● In this problem, a higher fitness level is better.
# ● Fitness_scores is a list containing the fitness score for each board state in the population.

# Step 4: Selection
# ● Combines fitness scores and population using zip(), pairs each board state with its fitness score.
# ● Sorts the population based on fitness (descending) because a higher score is better.
# ● Selects the top 50% of the population as parents for the next generation.
# ● These parents will be used to produce offspring in the next step (crossover).

# Step 5: Crossover
# ● Takes two parents (board) and produces an offspring.
# ● Randomly selects a subsequence from parent1 (from index start to end).
# ● Fills the rest of the child using parent2 in the order the queens appear, skipping any duplicates.
# ● Selects random pairs of parents from the previously selected parents list.
# ● Generates population_size offspring through crossover.
# ● Fills the new population with children, replacing the previous population.

# Step 6: Mutation
# ● Randomly selects two unique indices (idx1 and idx2) from the board.
# ● Swaps the queens at these two rows.
# ● Returns the mutated board.
# ● Since it only swaps existing columns, it preserves uniqueness.
# ● Loops through each route (child) in the new population.
# ● Applies mutation with a probability of 0.1 (10%): random.random() generates a random number between 0 and 1. If it is less than 0.1, mutation is applied.
# ● If mutation occurs, the board is slightly altered by swapping two queens.

# Step 7: Check Convergence Criteria

import random

n = 8
population_size = 10
mutation_rate = 0.1

def calculate_fitness(individual):
    non_attacking_pairs = 0
    total_pairs = n * (n - 1) // 2  # Maximum possible non-attacking pairs
    
    # Check for conflicts
    for i in range(n):
        for j in range(i + 1, n):
            # No same column or diagonal conflict
            if individual[i] != individual[j] and abs(individual[i] - individual[j]) != abs(i - j):
                non_attacking_pairs += 1
                
    return non_attacking_pairs / total_pairs

def create_random_individual():
    return random.sample(range(n), n)
  
population = [create_random_individual() for _ in range(population_size)]

# Evaluate fitness for each route in the population
fitness_scores = [calculate_fitness(individual) for individual in population]
print("Fitness Scores:", fitness_scores)

# Select the best routes (parents) based on fitness
def select_parents(population, fitness_scores):
  
    sorted_population = [board for _, board in sorted(zip(fitness_scores, population), reverse=True)]
    return sorted_population[:len(population) // 2]

parents = select_parents(population, fitness_scores)
print("Selected Parents:", parents)

def crossover(parent1, parent2):
    point = random.randint(1, n - 2) 
    child = parent1[:point] + parent2[point:]
    
    missing = set(range(n)) - set(child)
    for i in range(len(child)):
        if child.count(child[i]) > 1:
            child[i] = missing.pop()
            
    return child

# Create new population using crossover
new_population = []
for i in range(population_size):
    parent1, parent2 = random.sample(parents, 2)
    child = crossover(parent1, parent2)
    new_population.append(child)
    
print("New Population after Crossover:", new_population)

# Randomly swap two locations in a route
def mutate(route):
    individual = list(route)
    idx1, idx2 = random.sample(range(n), 2)
    individual[idx1], individual[idx2] = individual[idx2], individual[idx1]
    return individual

for i in range(len(new_population)):
    if random.random() < mutation_rate:
        new_population[i] = mutate(new_population[i])
        
print("Population after Mutation:", new_population)

def genetic_algorithm():
    population = [create_random_individual() for _ in range(population_size)]
    generation = 0
    best_fitness = 0
    
    while best_fitness < 1.0 and generation < 100:
        fitness_scores = [calculate_fitness(ind) for ind in population]
        best_fitness = max(fitness_scores)
        print(f"Generation {generation} Best Fitness: {best_fitness}")
        
        # Check for optimal solution
        if best_fitness == 1.0:
            break
            
        # Selection
        parents = select_parents(population, fitness_scores)
        
        # Crossover
        new_population = [crossover(random.choice(parents), random.choice(parents)) for _ in range(population_size)]
        
        # Mutation
        for i in range(len(new_population)):
            if random.random() < mutation_rate:
                new_population[i] = mutate(new_population[i])
                
        population = new_population
        generation += 1
        
    # Return the best solution
    best_individual = max(population, key=calculate_fitness)
    return best_individual, calculate_fitness(best_individual)

solution, fitness = genetic_algorithm()
print("Best Solution:", solution)
print("Best Fitness:", fitness)
