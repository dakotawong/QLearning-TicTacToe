import random
import pickle
import os
from collections import defaultdict

"""
Class that implements the Q-Learning Agent
"""
class Agent():

    """
    Epsilon: Exploration Rate (meaning probability agent returns random move).
    Discount: Discount Factor (factor at which future rewards are discounted).
    Learning Rate: Controls magnitude of incremental Q-Value updates.
    Q-Table: Dictionary that holds Q-Values for action-state pairs.
    """
    def __init__(self, epsilon = 0.7, discount = 0.9, learning_rate = 0.5):
        # Hyper Parameters
        self.epsilon = epsilon # Exploration Rate
        self.discount = discount # Discount Factor
        self.learning_rate = learning_rate # Learning Rate

        # Q-Table
        self.Q = {}
    
        # Initialize the Q-Table (Default Value = 0)
        for i in range(3):
            for j in range(3):
                self.Q[str([i,j])] = defaultdict(int)

    # Function to get the next action of the agent
    def getAction(self, state):
        # Get possible next actions
        actions = self.possibleActions(state)
        # If there are no possible next actions return None
        if (len(actions) == 0):
                return None
        # Decision Process
        if random.random() < self.epsilon:
            # Return a random next action (exploration)
            return random.choice(actions)
        else:
            # Get Q-Value for each possible next action
            q_values = [self.Q[str(action)][state] for action in actions]
            # Return the best action (greedy)
            return self.bestAction(state)

    # Function to update the agent's Q-Table (Learning Process)
    def update(self, next_state, action, reward, state):
        # Check if there is a next_state (See Q-learning equations for details)
        if (next_state != None):
            # Update Q-Table using next state
            y = reward + self.discount * (self.bestValue(state))
            self.Q[str(action)][state] += self.learning_rate * (y - self.Q[str(action)][state])
        else:
            # Update Q-Table without next state
            self.Q[str(action)][state] += self.learning_rate * (reward - self.Q[str(action)][state])

    # Function to get the max Q-Value of the next state from the Q-Table  
    def bestValue(self, state):
        # Get possible next actions
        actions = self.possibleActions(state)
        # Get Q-Value for each possible next action
        q_values = [self.Q[str(action)][state] for action in actions]
        # Return the values of the maximum Q-Value
        return max(q_values)

    # Function to get of best action from the Q-Table       
    def bestAction(self, state):
        # Get possible next actions
        actions = self.possibleActions(state)
        # Get Q-Value for each possible next action
        q_values = [self.Q[str(action)][state] for action in actions]
        # Return the action with the maximum Q-Value
        return actions[q_values.index(max(q_values))]
    
    # Function to get possible from a board state (state is in str format)
    def possibleActions(self, state):
        actions = []
        for (index, value) in enumerate(state):
            if (value == "*"):
                actions.append([index // 3, index % 3])
        return actions

    # Function to save the Q-Table (saves to ./models directory)
    def saveQ(self):
        try:
            # Save the Q-Table
            with open("./tables/q-table.pkl", 'wb') as file:
                pickle.dump(self.Q, file)
            print(f"Success: Q-Table was saved to './tables/q-table.pkl'")
        except:
            print("Failure: File could not be saved")
        return

    # Function to load a Q-table (loads from ./models directory)
    def loadQ(self):
        try:
            # Load the Q-Table
            with open("./tables/q-table.pkl", "rb") as file:
                Q = pickle.load(file)
                # Set the Q to the loaded Q-Table
                self.Q = Q
            print(f"Success: Q-Table loaded from './tables/q-table.pkl'")
        except:
            print("Failure: File could not be loaded")
        return 
        
            

                                
                                
                                
                        
                                
                                
                                
                                
                                
                                
                                
                                
                        
                                
                                
                        
                                
                                
                        
                                
                                
                                
                                
                                
                                
                                
                                
                        
                                
                                
                        
                                
                                
                        
                                
                                
                        
                                
                                
                        
                                
                                