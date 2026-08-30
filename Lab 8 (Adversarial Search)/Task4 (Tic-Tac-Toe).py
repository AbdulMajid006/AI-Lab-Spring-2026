# Task#4:
# Alpha-Beta in Tic-Tac-Toe AI:
# Implement a Tic-Tac-Toe AI Agent where:
# • AI = Max player (X)
# • Human = Min player (O)
# Task:
# 1. Implement:
#     a. Alpha-Beta pruning algorithm
#     b. Game board (3×3)
# 2. AI should:
#     a. Always play optimally
#     b. Never lose (win or draw guaranteed)
# 3. Display:
#     a. Game tree depth explored
#     b. Moves pruned during execution


import math

board = [' ' for _ in range(9)]

nodes_explored = 0
pruned_nodes = 0

def print_board():
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
    print()

def check_winner(b):
    wins = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for i, j, k in wins:
        if b[i] == b[j] == b[k] and b[i] != ' ':
            return b[i]
    return None

def is_draw(b):
    return ' ' not in b and check_winner(b) is None

def evaluate(b):
    w = check_winner(b)
    if w == 'X':
        return 10
    if w == 'O':
        return -10
    return 0

def alpha_beta(b, depth, alpha, beta, is_max):
    global nodes_explored, pruned_nodes
    nodes_explored += 1

    score = evaluate(b)
    if score != 0 or is_draw(b):
        return score

    if is_max:
        best = -math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'X'
                val = alpha_beta(b, depth + 1, alpha, beta, False)
                b[i] = ' '
                best = max(best, val)
                alpha = max(alpha, best)
                if beta <= alpha:
                    pruned_nodes += 1
                    break
        return best
    else:
        best = math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'O'
                val = alpha_beta(b, depth + 1, alpha, beta, True)
                b[i] = ' '
                best = min(best, val)
                beta = min(beta, best)
                if beta <= alpha:
                    pruned_nodes += 1
                    break
        return best

def best_move():
    best_val = -math.inf
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            val = alpha_beta(board, 0, -math.inf, math.inf, False)
            board[i] = ' '
            if val > best_val:
                best_val = val
                move = i
    return move

def play_game():
    global nodes_explored, pruned_nodes
    print_board()

    for t in range(9):
        if t % 2 == 0:
            m = best_move()
            board[m] = 'X'
        else:
            m = int(input())
            if board[m] == ' ':
                board[m] = 'O'
            else:
                continue

        print_board()

        if check_winner(board):
            w = check_winner(board)
            if w == 'X':
                print("X wins")
            else:
                print("O wins")
            break
        if is_draw(board):
            print("Draw")
            break

    print("Game tree depth explored (nodes):", nodes_explored)
    print("Moves pruned during execution:", pruned_nodes)

play_game()
