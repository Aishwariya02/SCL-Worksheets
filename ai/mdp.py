import numpy as np

class MarkovDecisionProcess:
    def __init__(self, num_states, num_actions, rewards, transitions, discount_factor):
        self.num_states = num_states
        self.num_actions = num_actions
        self.rewards = rewards
        self.transitions = transitions
        self.discount_factor = discount_factor
        
    def get_rewards(self, state, action):
        return self.rewards[state, action]
    
    def get_transition_probs(self, state, action):
        return self.transitions[state, action, :]
    
    def value_iteration(self, epsilon=0.0001):
        V = np.zeros(self.num_states)
        while True:
            delta = 0
            for s in range(self.num_states):
                v = V[s]
                V[s] = np.max([np.sum(self.get_transition_probs(s, a) * (self.get_rewards(s, a) + self.discount_factor * V)) 
                               for a in range(self.num_actions)])
                delta = max(delta, abs(v - V[s]))
            if delta < epsilon:
                break
        return V
    
num_states = 3
num_actions = 2
rewards = np.array([[0, 1], [2, 3], [4, 5]])
transitions = np.array([
    [[0.1, 0.9, 0], [0.4, 0.4, 0.2]],
    [[0.6, 0.4, 0], [0, 0.1, 0.9]],
    [[0, 0, 1], [0.3, 0.3, 0.4]]
])
discount_factor = 0.9
mdp = MarkovDecisionProcess(num_states, num_actions, rewards, transitions, discount_factor)

V = mdp.value_iteration()

print("Expected sum of discounted rewards:", V)
