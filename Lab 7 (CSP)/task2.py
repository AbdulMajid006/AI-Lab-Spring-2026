from ortools.sat.python import cp_model

model = cp_model.CpModel()

num_items = 10

Mon = model.new_int_var(0, num_items - 1, "Mon")
Tue = model.new_int_var(0, num_items - 1, "Tue")
Wed = model.new_int_var(0, num_items - 1, "Wed")
Thu = model.new_int_var(0, num_items - 1, "Thu")
Fri = model.new_int_var(0, num_items - 1, "Fri")

model.add(Fri <= 1)

model.add(Mon >= 2)
model.add(Thu >= 2)

model.add_all_different([Mon, Tue, Wed, Thu, Fri])

class SolutionPrinter(cp_model.CpSolverSolutionCallback):
    def __init__(self, variables):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.variables = variables
        self.solution_count = 0

    def on_solution_callback(self):
        self.solution_count += 1
        print(f"\nSolution {self.solution_count}:")
        for v in self.variables:
            print(f"{v}={self.value(v)}", end=" ")
        print()

solver = cp_model.CpSolver()
solution_printer = SolutionPrinter([Mon, Tue, Wed, Thu, Fri])

solver.parameters.enumerate_all_solutions = True
solver.solve(model, solution_printer)

print("\n0=SQ1, 1=SQ2, 2-6=Shirts, 7-9=Pants")
print("\nTotal solutions:", solution_printer.solution_count)