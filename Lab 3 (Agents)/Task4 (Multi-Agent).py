# Task#4:
# Multi-Agent Environment Simulation:
# A Simple Reflex Agent and a Learning-Based Agent operate together in the same environment.
# Their performance is compared based on task completion speed, action efficiency, and
# adaptability to environmental changes. This comparison highlights the advantages of learning-
# based agents in dynamic environments.

import random

class DynamicRoom:
    def __init__(self):
        self.state = random.choice(["Dirty", "Clean"])

    def perceive(self):
        return self.state

    def change(self):
        self.state = random.choice(["Dirty", "Clean"])

class ReflexAgent:
    def act(self, state):
        if state == "Dirty":
            return "Clean"
        return "Wait"

class LearningAgent:
    def __init__(self, actions):
        self.actions = actions
        self.q = {}
        self.alpha = 0.1
        self.gamma = 0.9
        self.epsilon = 0.1

    def get_q(self, state, action):
        return self.q.get((state, action), 0.0)

    def choose_action(self, state):
        if random.random() < self.epsilon:
            return random.choice(self.actions)
        return max(self.actions, key=lambda a: self.get_q(state, a))

    def learn(self, state, action, reward, next_state):
        old = self.get_q(state, action)
        future = max(self.get_q(next_state, a) for a in self.actions)
        self.q[(state, action)] = old + self.alpha * (reward + self.gamma * future - old)

def simulate(agent, room, steps=50, learning=False):
    total_reward = 0
    actions_count = 0

    for step in range(steps):
        state = room.perceive()

        if learning:
            action = agent.choose_action(state)
        else:
            action = agent.act(state)

        if action == "Clean" and state == "Dirty":
            reward = 10
            room.state = "Clean"
        elif action == "Clean" and state == "Clean":
            reward = -5
        else:
            reward = -1

        total_reward += reward
        actions_count += 1

        room.change() 

        if learning:
            next_state = room.perceive()
            agent.learn(state, action, reward, next_state)

    return total_reward, actions_count

room1 = DynamicRoom()
room2 = DynamicRoom()

reflex_agent = ReflexAgent()
learning_agent = LearningAgent(["Clean", "Wait"])

reflex_result = simulate(reflex_agent, room1)
learning_result = simulate(learning_agent, room2, learning=True)

print("Reflex Agent:")
print("Total Reward:", reflex_result[0])
print("Total Actions:", reflex_result[1])

print("\nLearning Agent:")
print("Total Reward:", learning_result[0])
print("Total Actions:", learning_result[1])
