import random

def calculate_conflicts(state):
    conflicts = 0
    n = len(state)

    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1

    return conflicts


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


def hill_climbing(initial_state):
    current_state = initial_state
    current_conflicts = calculate_conflicts(current_state)

    while True:
        neighbors = get_neighbors(current_state)

        best_neighbor = current_state
        best_conflicts = current_conflicts

        for neighbor in neighbors:
            conflicts = calculate_conflicts(neighbor)
            if conflicts < best_conflicts:
                best_neighbor = neighbor
                best_conflicts = conflicts

        if best_conflicts >= current_conflicts:
            return current_state, current_conflicts

        current_state = best_neighbor
        current_conflicts = best_conflicts


def random_restart_hill_climbing(n, max_restarts=20):
    for attempt in range(1, max_restarts + 1):
        initial_state = [random.randint(0, n - 1) for _ in range(n)]

        print(f"\nRestart {attempt}: Initial State = {initial_state}")

        solution, conflicts = hill_climbing(initial_state)

        print(f"Final State = {solution}")
        print(f"Conflicts = {conflicts}")

        if conflicts == 0:
            print("\nSolution Found")
            return solution, conflicts, attempt

    print("\nFailed to find solution within restart limit")
    return None, None, max_restarts


n = 8
solution, conflicts, attempts = random_restart_hill_climbing(n)

print("\nFinal Result:")
if solution:
    print(f"Solution: {solution}")
    print(f"Found in {attempts} restart(s)")
else:
    print("No solution found")