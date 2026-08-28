# Task#3:
# Emergency Evacuation Route Planning:
# PROBLEM: Implement an A* search algorithm to determine the fastest evacuation route in an emergency
# scenario. The algorithm must minimize travel time while avoiding blocked or unsafe routes.
# REQUIREMENTS
# • Implement A* with g(n), h(n), and f(n)
# • Update OPEN and CLOSED lists properly
# • Ignore unsafe or blocked edges
# • Always select node with minimum f(n)

graph = {
    'Entrance': {'Hallway1': 4, 'Hallway2': 3},
    'Hallway1': {'Stairs': 5, 'Elevator': 10},
    'Hallway2': {'Stairs': 6, 'RoomA': 7},
    'RoomA': {'Exit': 8},
    'Stairs': {'Exit': 3},
    'Elevator': {},   
    'Exit': {}
}

heuristic = {
    'Entrance': 10,
    'Hallway1': 7,
    'Hallway2': 6,
    'RoomA': 4,
    'Stairs': 2,
    'Elevator': 8,
    'Exit': 0
}

def a_star(graph, start, goal):

    OPEN = [(start, heuristic[start])]  
    CLOSED = set()

    g_cost = {start: 0}
    parent = {start: None}

    while OPEN:

        OPEN.sort(key=lambda x: x[1])
        current, f_value = OPEN.pop(0)

        if current in CLOSED:
            continue

        print(current, end=" ")
        CLOSED.add(current)

        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            path.reverse()
            print("\nFastest Evacuation Path:", path)
            return

        for neighbor, cost in graph[current].items():

            if cost <= 0:
                continue

            new_g = g_cost[current] + cost
            f = new_g + heuristic[neighbor]

            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                parent[neighbor] = current
                OPEN.append((neighbor, f))

    print("\nNo safe evacuation route found")


print("Evacuation Search Order:")
a_star(graph, 'Entrance', 'Exit')
