# Hill Climbing is a heuristic search algorithm that focuses on finding the optimal solution by making incremental changes to
# an existing solution and then evaluating whether the new solution is better than the
# current one.
# 1. Start at the initial node and evaluate its heuristic score.
# 2. Generate one neighboring node at a time.
# 3. If the neighbor's score is better than the current node, move to that neighbor, else generate the next neighbor.
# 4. If no neighbor has a better score, terminate the search.
# 5. Return the current node as the solution.

# Solving N-Queens Using Simple Hill Climbing:
# We aim to place N queens on an N×N chessboard such that no two queens attack each
# other.
# 1. State Representation: Each row has one queen, and the column position is
# stored in a list.
# Example for N=4: [1, 3, 0, 2] means:
#   ○ Queen in Row 0 is in Column 1.
#   ○ Queen in Row 1 is in Column 3, and so on.
# 2. Heuristic Function: Counts the number of pairs of queens attacking each other.
# 3. Neighbor Generation: Moves a queen in a row to different columns to create
# neighbors.

import random

def calculate_conflicts(state):
    print(state)
    conflicts = 0
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            # Check same column or diagonal
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1
    return conflicts

# Generate neighbors by moving one queen at a time
def get_neighbors(state):
    neighbors = []
    n = len(state)
    for row in range(n):
        for col in range(n):
            if col != state[row]:
                new_state = list(state)
                new_state[row] = col
                neighbors.append(new_state)
    return neighbors

def simple_hill_climbing(n):
  
    current_state = [random.randint(0, n - 1) for _ in range(n)]
    current_conflicts = calculate_conflicts(current_state)
    
    while True:
        neighbors = get_neighbors(current_state)
        next_state = None
        next_conflicts = current_conflicts
        
        # Find the first better neighbor
        for neighbor in neighbors:
            neighbor_conflicts = calculate_conflicts(neighbor)
            if neighbor_conflicts < next_conflicts:
                next_state = neighbor
                next_conflicts = neighbor_conflicts
                break  
                
        if next_conflicts >= current_conflicts:
            break
            
        # Move to the better neighbor
        current_state = next_state
        current_conflicts = next_conflicts
        
    return current_state, current_conflicts

n = 8 
solution, conflicts = simple_hill_climbing(n)  # Fixed parameter pass from 4 to n

if conflicts == 0:
    print(f"Solution found for {n}-Queens problem:")
    print(solution)
else:
    print(f"Could not find a solution. Stuck at state with {conflicts} conflicts:")
    print(solution)
