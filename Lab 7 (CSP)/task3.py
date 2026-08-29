from ortools.sat.python import cp_model

model = cp_model.CpModel()

n = 6

grid = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(model.new_int_var(1, 6, f"cell_{i}_{j}"))
    grid.append(row)

puzzle = [
    [0, 0, 6, 2, 5, 0],
    [0, 0, 0, 4, 6, 0],
    [0, 1, 2, 0, 0, 0],
    [5, 6, 0, 0, 0, 4],
    [0, 0, 4, 3, 0, 2],
    [3, 0, 0, 5, 0, 6]
]

for i in range(n):
    for j in range(n):
        if puzzle[i][j] != 0:
            model.add(grid[i][j] == puzzle[i][j])

for i in range(n):
    model.add_all_different(grid[i])

for j in range(n):
    model.add_all_different([grid[i][j] for i in range(n)])

for i in range(0, n, 2):
    for j in range(0, n, 3):
        block = []
        for di in range(2):
            for dj in range(3):
                block.append(grid[i + di][j + dj])
        model.add_all_different(block)

solver = cp_model.CpSolver()
status = solver.solve(model)

if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    print("Solved Sudoku:\n")
    for i in range(n):
        for j in range(n):
            print(solver.value(grid[i][j]), end=" ")
        print()
else:
    print("No solution found")