# Task#2:
# Utility-Based Decision Agent:
# A Utility-Based Agent selects actions by maximizing utility. The agent can clean the room, move
# to the next room, or do nothing. Each action is assigned a utility value based on the
# environment’s state. The agent chooses the action with the highest utility and displays the
# selected action, its utility value, and the total accumulated utility.

class UtilityBasedAgent:
    def __init__(self, environment):
        self.environment = environment
        self.position = 0
        self.total_utility = 0

    def goal_achieved(self):
        return all(room == "Clean" for room in self.environment)

    def perceive(self):
        return self.environment[self.position]

    def possible_actions(self):
        return ["Clean", "Move", "Do Nothing"]

    def utility(self, action):
        current_room = self.perceive()

        if action == "Clean":
            if current_room == "Dirty":
                return 10  
            else:
                return -2  
        elif action == "Move":
            if self.position < len(self.environment) - 1:
                return 3
            else:
                return -1 
        elif action == "Do Nothing":
            return -5 

    def choose_action(self):
        actions = self.possible_actions()
        utilities = {action: self.utility(action) for action in actions}
        best_action = max(utilities, key=utilities.get)
        return best_action, utilities[best_action]

    def act(self):
        action, utility_value = self.choose_action()

        print("\n")
        print(f"Position: {self.position}")
        print(f"Room Status: {self.environment[self.position]}")
        print(f"Chosen Action: {action}")
        print(f"Utility of Action: {utility_value}")

        if action == "Clean" and self.environment[self.position] == "Dirty":
            self.environment[self.position] = "Clean"

        elif action == "Move" and self.position < len(self.environment) - 1:
            self.position += 1

        self.total_utility += utility_value

        print(f"Total Accumulated Utility: {self.total_utility}")
        print("Environment:", self.environment)

rooms = ["Dirty", "Dirty", "Clean", "Dirty"]
agent = UtilityBasedAgent(rooms)
while not agent.goal_achieved():
    agent.act()
print("Final Utility:", agent.total_utility)
