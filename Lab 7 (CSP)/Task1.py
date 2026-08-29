# Task#1:
# Graph Coloring:
# Graph coloring is a problem in which we assign colors to the vertices/nodes of a
# graph such that not two adjacent vertices have the same color.
# Considering the following graph, implement CSP solution to find all the possible
# ways of graph coloring using Red, Green, and Blue colors.

from ortools.sat.python import cp_model

model = cp_model.CpModel()

num_vals = 3

A = model.new_int_var(0, num_vals - 1, "A")
B = model.new_int_var(0, num_vals - 1, "B")
C = model.new_int_var(0, num_vals - 1, "C")
D = model.new_int_var(0, num_vals - 1, "D")
E = model.new_int_var(0, num_vals - 1, "E")

model.add(A != B)
model.add(A != E)
model.add(B != C)
model.add(B != D)
model.add(C != D)
model.add(D != E)

class SolutionPrinter(cp_model.CpSolverSolutionCallback):
    def __init__(self, variables):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.variables = variables
        self.solution_count = 0

    def on_solution_callback(self):
        self.solution_count += 1
        for v in self.variables:
            print(f"{v}={self.value(v)}", end=" ")
        print()

solver = cp_model.CpSolver()
solution_printer = SolutionPrinter([A, B, C, D, E])

solver.parameters.enumerate_all_solutions = True
solver.solve(model, solution_printer)

print("Total solutions:", solution_printer.solution_count)
