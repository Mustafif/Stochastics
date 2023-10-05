import numpy as np
import pandas as pd

class Weather: 
    def __init__(self, filename): 
        self.data = pd.read_excel(filename, usecols=[1])
        self.states = [1, 2, 3]
    def transition_matrix(self): 
        # Create an empty transition matrix
        transition_matrix = np.zeros((len(self.states), len(self.states)), dtype=float)
        # Loop through the data and calculate transition counts
        for i in range(len(self.data) - 1):
            from_state = self.data[i]
            to_state = self.data[i + 1]
            transition_matrix[from_state - 1][to_state - 1] += 1
        # Normalize the transition matrix to get probabilities
        transition_matrix /= np.sum(transition_matrix, axis=1, keepdims=True)
        return transition_matrix


weather = Weather('./mchdata3.xlsx')
transition_matrix = weather.transition_matrix()
# Print the transition matrix
print("Transition Probability Matrix:")
print(transition_matrix)

# Calculate the probability that Sunday is sunny given that Friday is sunny
probability_sunday_sunny = transition_matrix[0][0]
print("Probability that Sunday is sunny given that Friday is sunny:", probability_sunday_sunny)
