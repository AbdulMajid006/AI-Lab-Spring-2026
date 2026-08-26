import random
import string

alphabets = list(string.ascii_uppercase)
random.shuffle(alphabets)

tree = {}

for i in range(26):
    left_index = 2 * i + 1
    right_index = 2 * i + 2

    children = []

    if left_index < 26:
        children.append(alphabets[left_index])
    if right_index < 26:
        children.append(alphabets[right_index])

    tree[alphabets[i]] = children

start_node = alphabets[0]
goal_node = 'G'

def bfs(graph, start, goal):
    visited = []
    queue = []

    visited.append(start)
    queue.append(start)

    while queue:
        node = queue.pop(0)
        print(node, end=" ")

        if node == goal:
            print("\nGoal found")
            return

        for neighbour in graph.get(node, []):
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

    print("\nGoal not found")

def dfs(graph, start, goal):
    visited = []
    stack = []

    visited.append(start)
    stack.append(start)

    while stack:
        node = stack.pop()
        print(node, end=" ")

        if node == goal:
            print("\nGoal found")
            return

        for neighbour in reversed(graph.get(node, [])):
            if neighbour not in visited:
                visited.append(neighbour)
                stack.append(neighbour)

    print("\nGoal not found")

def dls(graph, start, goal, depth_limit):

    def dfs_recursive(node, depth, path):
        if depth > depth_limit:
            return None

        path.append(node)
        print(f"Visiting: {node} at depth {depth}")

        if node == goal:
            return path

        for neighbour in graph.get(node, []):
            result = dfs_recursive(neighbour, depth + 1, path)
            if result:
                return result

        path.pop()
        return None

    result = dfs_recursive(start, 0, [])

    if result:
        print("Goal found. Path:", " -> ".join(result))
    else:
        print("Goal not found within depth limit")

def iterative_deepening(graph, start, goal, max_depth):

    def dls_ids(node, goal, depth, path):
        if depth == 0:
            return False

        if node == goal:
            path.append(node)
            return True

        for child in graph.get(node, []):
            if dls_ids(child, goal, depth - 1, path):
                path.append(node)
                return True

        return False

    for depth in range(max_depth + 1):
        print(f"\nDepth Level: {depth}")
        path = []

        if dls_ids(start, goal, depth, path):
            print("Path to goal:", " -> ".join(reversed(path)))
            return

    print("Goal not found")

weighted_tree = {}

for parent in tree:
    weighted_tree[parent] = {}
    for child in tree[parent]:
        weighted_tree[parent][child] = random.randint(1, 10)


def ucs(graph, start, goal):

    frontier = [(start, 0)] 
    visited = set()
    cost_so_far = {start: 0}
    came_from = {start: None}

    while frontier:

        frontier.sort(key=lambda x: x[1])
        current_node, current_cost = frontier.pop(0)

        if current_node in visited:
            continue

        visited.add(current_node)

        if current_node == goal:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = came_from[current_node]

            path.reverse()

            print("Goal found")
            print("Path:", path)
            print("Total Cost:", current_cost)
            return

        for neighbor, cost in graph[current_node].items():
            new_cost = current_cost + cost

            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                came_from[neighbor] = current_node
                frontier.append((neighbor, new_cost))

    print("Goal not found")

print("\nGenerated Binary Tree:")
print(tree)

print("\nStart Node:", start_node)
print("Goal Node:", goal_node)

print("\nBreadth First Search")
bfs(tree, start_node, goal_node)

print("\nDepth First Search")
dfs(tree, start_node, goal_node)

print("\nDepth Limited Search (limit=3)")
dls(tree, start_node, goal_node, 3)

print("\nIterative Deepening Search (depth=5)")
iterative_deepening(tree, start_node, goal_node, 5)

print("\nUniform Cost Search")
ucs(weighted_tree, start_node, goal_node)