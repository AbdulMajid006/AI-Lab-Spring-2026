# Task#1:
# Campus Navigation System:
# PROBLEM:
# Design a Best-First Search algorithm to find the most promising route between two
# locations inside a university campus.
# Each location is represented as a node, and heuristic values represent the estimated walking
# distance to the destination.
# REQUIREMENTS
# • Implement Best-First Search using a priority queue
# • Use heuristic values to select the next building
# • Maintain OPEN and CLOSED lists
# • Stop search once destination building is reached

from queue import PriorityQueue

campus_graph = {
    'Gate': [('Library', 6), ('Cafeteria', 8)],
    'Library': [('Lab', 4), ('Admin', 3)],
    'Cafeteria': [('Hostel', 7)],
    'Lab': [('Classroom', 1)],
    'Admin': [('Classroom', 2)],
    'Hostel': [],
    'Classroom': []
}

def best_first_search(graph, start, goal):

    OPEN = PriorityQueue() 
    CLOSED = set()  

    OPEN.put((0, start)) 

    while not OPEN.empty():

        cost, node = OPEN.get()

        if node not in CLOSED:

            print(node, end=" ")
            CLOSED.add(node)

            if node == goal:
                print("\nDestination reached")
                return True

            for neighbor, heuristic in graph[node]:
                if neighbor not in CLOSED:
                    OPEN.put((heuristic, neighbor))

    print("\nDestination not reachable")
    return False


print("Campus Navigation Path:")
best_first_search(campus_graph, 'Gate', 'Classroom')
