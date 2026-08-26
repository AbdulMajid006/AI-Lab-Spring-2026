from collections import deque

start_state = (
    (7, 2, 4),
    (5, 0, 6),
    (8, 3, 1)
)

goal_state = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8)
)

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


def get_neighbors(state):
    neighbors = []
    x, y = find_blank(state)

    directions = [(-1,0),(1,0),(0,-1),(0,1)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [list(row) for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(tuple(tuple(row) for row in new_state))

    return neighbors

def bfs(start, goal):

    queue = deque()
    queue.append(start)

    visited = set()
    visited.add(start)

    parent = {start: None}

    while queue:
        current = queue.popleft()

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            path.reverse()
            return path

        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)

    return None

class GoalBasedAgent:

    def __init__(self, goal):
        self.goal = goal

    def act(self, start_state):
        path = bfs(start_state, self.goal)

        if path:
            print("\nGoal Reached\n")
            print("Number of Moves:", len(path) - 1)
            print("\nFinal State:")
            for row in path[-1]:
                print(row)
        else:
            print("No solution found")

agent = GoalBasedAgent(goal_state)
agent.act(start_state)