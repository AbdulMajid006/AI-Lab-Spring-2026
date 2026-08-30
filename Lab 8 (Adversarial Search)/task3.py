import math

GOAL = 5

class State:
    def __init__(self, pos_max, pos_min):
        self.pos_max = pos_max
        self.pos_min = pos_min

def heuristic(state):
    if state.pos_max == GOAL:
        return 10
    if state.pos_min == state.pos_max:
        return -10
    return -(abs(GOAL - state.pos_max))

def get_moves(state, is_max):
    moves = []
    if is_max:
        if state.pos_max + 1 <= GOAL:
            moves.append(State(state.pos_max + 1, state.pos_min))
        if state.pos_max - 1 >= 0:
            moves.append(State(state.pos_max - 1, state.pos_min))
    else:
        if state.pos_min + 1 <= GOAL:
            moves.append(State(state.pos_max, state.pos_min + 1))
        if state.pos_min - 1 >= 0:
            moves.append(State(state.pos_max, state.pos_min - 1))
    return moves

def minimax(state, depth, is_max):
    if depth == 0 or state.pos_max == GOAL or state.pos_min == state.pos_max:
        h = heuristic(state)
        print("Leaf:", (state.pos_max, state.pos_min), "H=", h)
        return h

    if is_max:
        best = -math.inf
        for move in get_moves(state, True):
            val = minimax(move, depth - 1, False)
            best = max(best, val)
        return best
    else:
        best = math.inf
        for move in get_moves(state, False):
            val = minimax(move, depth - 1, True)
            best = min(best, val)
        return best

def best_move(state, depth):
    best_val = -math.inf
    best_state = None
    for move in get_moves(state, True):
        val = minimax(move, depth - 1, False)
        if val > best_val:
            best_val = val
            best_state = move
    return best_state, best_val

states = [State(0, 2), State(1, 3), State(2, 4)]

for d in [2, 3]:
    print("\nDepth =", d)
    for s in states:
        move, val = best_move(s, d)
        print("Start:", (s.pos_max, s.pos_min), "-> Move to:", (move.pos_max, move.pos_min), "Value:", val)