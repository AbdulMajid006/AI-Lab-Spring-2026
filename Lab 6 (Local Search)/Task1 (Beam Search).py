# Task#1:
# Beam Search with Dynamic Beam Width:
# PROBLEM:
# Modify the Beam Search algorithm so that the beam width automatically increases if the
# search is not progressing toward the goal.
# REQUIREMENTS
# 1. Use the provided graph or create a larger graph with at least 15 nodes.
# 2. Implement Beam Search with the following behavior:
#     • Start with beam width = 2.
#     • If the goal is not found after 3 levels, increase the beam width by 1.
#     • Maximum beam width allowed = 5.
# 3. Track and print:
#     • Beam nodes at each level.
#     • Current beam width.
#     • Final path and total cost.

import heapq

graph = {
    'S': [('A', 2), ('B', 4), ('C', 3)],
    'A': [('D', 5), ('E', 6)],
    'B': [('F', 2), ('G', 4)],
    'C': [('H', 7), ('I', 3)],
    'D': [('J', 4)],
    'E': [('K', 3)],
    'F': [('L', 6)],
    'G': [('M', 5)],
    'H': [('N', 2)],
    'I': [('O', 4)],
    'J': [], 'K': [], 'L': [], 'M': [],
    'N': [], 'O': []
}

def dynamic_beam_search(start, goal):
    beam_width = 2
    max_beam_width = 5
    level = 0

    beam = [(0, [start])]

    while beam:
        print(f"\nLevel {level}")
        print(f"Current Beam Width: {beam_width}")
        print("Beam Nodes:", [path for cost, path in beam])

        candidates = []

        for cost, path in beam:
            current = path[-1]

            if current == goal:
                print("\nGoal Found")
                return path, cost

            for neighbor, edge_cost in graph.get(current, []):
                new_cost = cost + edge_cost
                new_path = path + [neighbor]
                candidates.append((new_cost, new_path))

        if not candidates:
            break

        beam = heapq.nsmallest(beam_width, candidates, key=lambda x: x[0])

        level += 1

        if level % 3 == 0 and beam_width < max_beam_width:
            beam_width += 1
            print(f"Beam width increased to {beam_width}")

    return None, float('inf')


start_node = 'S'
goal_node = 'O'

path, cost = dynamic_beam_search(start_node, goal_node)

print("\nFinal Result:")
if path:
    print("Path found:", " → ".join(path))
    print("Total cost:", cost)
else:
    print("No path found")
