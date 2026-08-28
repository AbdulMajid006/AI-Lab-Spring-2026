# Beam Search:
# Beam Search is a heuristic search algorithm that navigates a search space by
# systematically expanding the most promising nodes within a constrained set.
# 1. Initialize the beam with the start state.
# 2. Set the beam width k to a predefined value.
# 3. While the termination condition is not met:
#     ○ Generate all possible successor states for each state in the beam.
#     ○ Calculate a heuristic score for each successor state.
#     ○ Rank the successor states based on their scores.
#     ○ Retain the top k states and discard the rest.
#     ○ Update the beam with the retained states.
# 4. Return the best path based on the final scores.

import heapq

graph = {
    'S': [('A', 3), ('B', 6), ('C', 5)],
    'A': [('D', 9), ('E', 8)],
    'B': [('F', 12), ('G', 14)],
    'C': [('H', 7)],
    'H': [('I', 5), ('J', 6)],
    'I': [('K', 1), ('L', 10), ('M', 2)],
    'D': [], 'E': [],
    'F': [], 'G': [],
    'J': [], 'K': [],
    'L': [], 'M': []
}

def beam_search(start, goal, beam_width=2):
    beam = [(0, [start])] 
    
    while beam:
        candidates = []
        # Expand each path in the beam
        for cost, path in beam:
            current_node = path[-1]
            if current_node == goal:
                return path, cost 
            
            # Generate successors
            for neighbor, edge_cost in graph.get(current_node, []):
                new_cost = cost + edge_cost
                new_path = path + [neighbor]
                candidates.append((new_cost, new_path))
                
        if not candidates:
            break
            
        # Select top-k paths based on the lowest cumulative cost
        beam = heapq.nsmallest(beam_width, candidates, key=lambda x: x[0])
        
    return None, float('inf') 

start_node = 'S'
goal_node = 'L'
beam_width = 3

path, cost = beam_search(start=start_node, goal=goal_node, beam_width=beam_width)

if path:
    print(f"Path found: {' -> '.join(path)} with total cost: {cost}")
else:
    print("No path found.")
