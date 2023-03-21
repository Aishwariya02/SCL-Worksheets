import numpy as np

class HMM:
    def __init__(self, A, B, pi):
        self.A = A   # transition matrix
        self.B = B   # emission matrix
        self.pi = pi # initial distribution
        
        self.N = A.shape[0] # number of states
        self.M = B.shape[1] # number of observation symbols
        
    def forward(self, obs):
        T = len(obs)
        alpha = np.zeros((T, self.N))
        
        # compute initial alpha
        alpha[0] = self.pi * self.B[:, obs[0]]
        
        # compute alpha for each time step t > 0
        for t in range(1, T):
            for j in range(self.N):
                alpha[t, j] = np.sum(alpha[t-1] * self.A[:, j]) * self.B[j, obs[t]]
        
        return alpha.sum(axis=1)[-1]
    
    def viterbi(self, obs):
        T = len(obs)   # length of the observation sequence
        N = self.A.shape[0]   # number of states
    
        # Initialize the Viterbi table and backpointer table
        viterbi = np.zeros((T, N))
        backpointers = np.zeros((T, N), dtype=int)
    
        # Initialize the first column of the Viterbi table
        viterbi[0, :] = self.pi * self.B[:, obs[0]]
    
        # Fill in the rest of the Viterbi table and backpointer table
        for t in range(1, T):
            for j in range(N):
                # Compute the maximum probability and backpointer for state j at time t
                max_prob = 0
                max_backpointer = 0
                for i in range(N):
                    prob = viterbi[t-1, i] * self.A[i, j] * self.B[j, obs[t]]
                    if prob > max_prob:
                        max_prob = prob
                        max_backpointer = i
                viterbi[t, j] = max_prob
                backpointers[t, j] = max_backpointer
    
        # Trace back through the backpointer table to find the most likely sequence of states
        states = np.zeros(T, dtype=int)
        states[T-1] = np.argmax(viterbi[T-1, :])
        for t in range(T-2, -1, -1):
            states[t] = backpointers[t+1, states[t+1]]
    
        return states

# Define the HMM parameters (example values only, replace with actual parameters)
transition_probs = np.array([[0.4, 0.5], [0.4, 0.6]])   
emission_probs = np.array([[0.2, 0.3, 0.3, 0.2], [0.3, 0.2, 0.2, 0.3]])   
initial_distr = np.array([0.5, 0.5])  

# Create the HMM object
hmm = HMM(transition_probs, emission_probs, initial_distr)

# (a) Compute the probability of observing the sequence GGCA
obs = [1, 1, 0, 2]   # GGCA represented as integers
prob = hmm.forward(obs)
print("Probability of observing sequence GGCA = {:.4f}".format(prob))

# (b) Find the most likely sequence of states that generated GGCACTGAA
obs = [1, 1, 0, 2, 0, 3, 1, 2, 2]   # GGCACTGAA represented as integers
states = hmm.viterbi(obs)
finalstates = []
for i in states:
    if i == 0:
        finalstates.append('H')
    elif i == 1:
        finalstates.append('L')
print("Most likely sequence of states for GGCACTGAA = {}".format(finalstates))
