# Task#1:
# Goal-Based Navigation Agent:
# This task involves designing a Goal-Based Agent in a one-dimensional environment where some
# rooms are dirty. The agent’s goal is to clean all rooms and it continues operating until this goal is
# achieved. At each step, the agent observes the environment, updates its goal if needed, and takes
# an action. The current percept, goal, and action are displayed at every step.

class GoalBasedAgent:
    def __init__(self, environment):
        self.environment = environment 
        self.position = 0               
        self.goal = "Clean all rooms"

    def is_goal_achieved(self):
        return all(room == "Clean" for room in self.environment)

    def perceive(self):
        return {
            "position": self.position,
            "status": self.environment[self.position]
        }

    def act(self):
        percept = self.perceive()
        print("Percept:", percept)
        print("Goal:", self.goal)

        if percept["status"] == "Dirty":
            self.environment[self.position] = "Clean"
            action = "Clean"
        else:
            if self.position < len(self.environment) - 1:
                self.position += 1
                action = "Move Right"
            else:
                self.position -= 1
                action = "Move Left"

        print("Action:", action)
        print("Environment:", self.environment)

rooms = ["Dirty", "Clean", "Dirty", "Dirty", "Clean"]
agent = GoalBasedAgent(rooms)
while not agent.is_goal_achieved():
    agent.act()

print("\nAll rooms are cleaned")
