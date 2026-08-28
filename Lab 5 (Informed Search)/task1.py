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