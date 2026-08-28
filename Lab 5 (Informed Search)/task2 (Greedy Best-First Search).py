# Task#2:
# Robot Object Collection Problem:
# PROBLEM:
# A robot is placed in a grid environment containing multiple objects.
# Using Greedy Best-First Search, the robot must collect the closest object first based on
# heuristic distance.
# REQUIREMENTS
# • Use Greedy BFS with f(n) = h(n)
# • Always move toward the nearest object
# • Mark collected objects and continue search
# • Avoid revisiting cells

from queue import PriorityQueue

grid = [
    [0, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 0, 0]
]

start = (0, 0)

objects = [(0, 3), (3, 0), (3, 3)]


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def greedy_bfs(grid, start, goal):

    rows, cols = len(grid), len(grid[0])
    pq = PriorityQueue()
    pq.put((0, start))

    visited = set()
    parent = {start: None}

    while not pq.empty():

        _, current = pq.get()

        if current in visited:
            continue

        visited.add(current)

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            path.reverse()
            return path

        x, y = current

        moves = [(1,0), (-1,0), (0,1), (0,-1)]

        for dx, dy in moves:
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols:
                if grid[nx][ny] == 0 and (nx, ny) not in visited:

                    neighbor = (nx, ny)
                    parent[neighbor] = current

                    h = heuristic(neighbor, goal)
                    pq.put((h, neighbor))

    return None


current_pos = start

while objects:

    objects.sort(key=lambda obj: heuristic(current_pos, obj))
    target = objects.pop(0)

    print(f"\nRobot moving to object at {target}")

    path = greedy_bfs(grid, current_pos, target)

    if path:
        print("Path:", path)
        current_pos = target
        print("Object collected")
    else:
        print("Object unreachable")

print("\nAll objects collected")
