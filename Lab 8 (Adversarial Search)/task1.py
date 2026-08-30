import math

class Node:
    def __init__(self, value=None):
        self.value = value
        self.children = []
        self.minimax_value = None

def minimax(node, maximizing_player):
    if not node.children:
        return node.value

    if maximizing_player:
        max_eval = -math.inf
        for child in node.children:
            eval = minimax(child, False)
            max_eval = max(max_eval, eval)
        node.minimax_value = max_eval
        return max_eval
    else:
        min_eval = math.inf
        for child in node.children:
            eval = minimax(child, True)
            min_eval = min(min_eval, eval)
        node.minimax_value = min_eval
        return min_eval

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

D.children = [Node(2), Node(4)]
E.children = [Node(7), Node(8)]
F.children = [Node(1), Node(3)]
G.children = [Node(-2), Node(0)]

result = minimax(A, True)

print("D:", D.minimax_value)
print("E:", E.minimax_value)
print("F:", F.minimax_value)
print("G:", G.minimax_value)
print("B:", B.minimax_value)
print("C:", C.minimax_value)
print("A:", A.minimax_value)

best_move = "B" if B.minimax_value > C.minimax_value else "C"
print("Optimal Value:", result)
print("Best Move:", best_move)