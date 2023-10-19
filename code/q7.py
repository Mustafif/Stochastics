import pandas as pd
import numpy as np

# Read the data from the Excel file
data = pd.read_excel('mchdata3.xlsx')

# Assuming the second column contains weather states (1, 2, 3)
weather_states = data.iloc[:, 1].tolist()
# Define the states as numbers
states = [1, 2, 3]
# Initialize the transition probability matrix
transition_matrix = np.zeros((len(states), len(states)))
# Calculate transition counts
for i in range(len(weather_states) - 1):
    from_state = weather_states[i]
    to_state = weather_states[i + 1]
    transition_matrix[from_state - 1][to_state - 1] += 1
# Calculate transition probabilities
transition_probabilities = transition_matrix / transition_matrix.sum(axis=1)[:, np.newaxis]
# Print transition probabilities
print("Transition Probabilities:")
for from_state in states:
    print(f"From State {from_state}:")
    for to_state, probability in enumerate(transition_probabilities[from_state - 1]):
        print(f"  To State {to_state + 1}: Probability = {probability:.2f}")
