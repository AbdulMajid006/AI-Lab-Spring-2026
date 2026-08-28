# Task#3:
# Learning Agent Performance Improvement:
# This task focuses on a Learning-Based Agent that improves its behavior over time using
# rewards. The agent balances exploration and exploitation to learn better actions. As the
# simulation runs, the agent’s performance improves. The final Q-table is displayed to show the
# learned action values.

import random

class LearningAgent:
    def __init__(self, actions):
        self.actions = actions
        self.q_values = {}
        self.alpha = 0.1     
        self.gamma = 0.9   
        self.epsilon = 0.1  

    def q(self, state, action):
        return self.q_values.get((state, action), 0.0)

    def select_action(self, state):
        if random.random() < self.epsilon:
            return random.choice(self.actions)
        else:
            best = max(self.actions, key=lambda a: self.q(state, a))
            return best

    def learn(self, state, action, reward, next_state):
        current_q = self.q(state, action)
        best_future_q = max(self.q(next_state, a) for a in self.actions)

        updated_q = current_q + self.alpha * (
            reward + self.gamma * best_future_q - current_q
        )

        self.q_values[(state, action)] = updated_q


class SimpleRoom:
    def __init__(self):
        self.state = random.choice(["Dirty", "Clean"])

    def get_state(self):
        return self.state

    def execute(self, action):
        if action == "Clean":
            if self.state == "Dirty":
                self.state = "Clean"
                return 10
            else:
                return -5
        elif action == "Wait":
            return -1


def run_simulation(agent, environment, iterations=200):
    for step in range(iterations):

        current_state = environment.get_state()
        chosen_action = agent.select_action(current_state)

        reward = environment.execute(chosen_action)

        next_state = random.choice(["Dirty", "Clean"])
        environment.state = next_state

        agent.learn(current_state, chosen_action, reward, next_state)

    print("\nLearned Q-Values:")
    for (state, action), value in agent.q_values.items():
        print(f"State: {state}, Action: {action}  {round(value,2)}")

my_agent = LearningAgent(["Clean", "Wait"])
my_room = SimpleRoom()
run_simulation(my_agent, my_room)
