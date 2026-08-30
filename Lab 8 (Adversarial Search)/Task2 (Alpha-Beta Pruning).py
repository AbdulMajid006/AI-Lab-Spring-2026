# Task#2:
# Alpha-Beta Pruning on Game Tree
# Use the same tree from Task 1.
# • Apply Alpha-Beta pruning step-by-step
# • Track:
#     o Alpha (α) and Beta (β) values at each node
# • Identify:
#     o Pruned branches
#     o Number of nodes evaluated vs Minimax
# • Compare efficiency:
#     o Nodes explored (Minimax vs Alpha-Beta)


import math

class Node:
    def __init__(self, value=None):
        self.value = value
        self.children = []
        self.minimax_value = None

visited_nodes = 0

def alpha_beta(node, depth, alpha, beta, maximizing_player):
    global visited_nodes
    visited_nodes += 1

    if not node.children:
        return node.value

    if maximizing_player:
        value = -math.inf
        for child in node.children:
            value = max(value, alpha_beta(child, depth-1, alpha, beta, False))
            alpha = max(alpha, value)
            if beta <= alpha:
                print("Pruned:", child.value)
                break
        node.minimax_value = value
        print(node.value, "->", "α:", alpha, "β:", beta, "val:", value)
        return value
    else:
        value = math.inf
        for child in node.children:
            value = min(value, alpha_beta(child, depth-1, alpha, beta, True))
            beta = min(beta, value)
            if beta <= alpha:
                print("Pruned:", child.value)
                break
        node.minimax_value = value
        print(node.value, "->", "α:", alpha, "β:", beta, "val:", value)
        return value


A = Node('A')
B = Node('B')
C = Node('C')
A.children = [B, C]

D = Node('D')
E = Node('E')
F = Node('F')
G = Node('G')

B.children = [D, E]
C.children = [F, G]

D.children = [Node(4), Node(7)]
E.children = [Node(2), Node(8)]
F.children = [Node(3), Node(6)]
G.children = [Node(1), Node(5)]

result = alpha_beta(A, 3, -math.inf, math.inf, True)

print("\nD:", D.minimax_value)
print("E:", E.minimax_value)
print("F:", F.minimax_value)
print("G:", G.minimax_value)
print("B:", B.minimax_value)
print("C:", C.minimax_value)
print("A:", A.minimax_value)

best_move = "B" if B.minimax_value > C.minimax_value else "C"
print("Optimal Value:", result)
print("Best Move:", best_move)

print("Nodes evaluated:", visited_nodes)
