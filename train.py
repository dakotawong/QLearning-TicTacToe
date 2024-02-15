from src.agent import Agent 
from src.env import TicTacToe

"""
This file can be used to train the Q-Learning Agent
"""

def train(agent, num_episodes):

    # Declare opponent to train agent against (Epsilon of 1 makes the agent pick actions randomly)
    opponent = Agent(epsilon=1)

    # Declare the training environment
    env = TicTacToe(agent, opponent)

    # Agent now trains acrosses specified number of episodes
    print("Training...")
    for i in range(num_episodes):
        env.playGame()
    
    # Training Complete
    print("Training Complete")


if __name__ == "__main__":

    # Agent Hyperparameters (Tweak These)
    epsilon = 0.7
    Learning_rate = 0.5
    discount = 0.9

    # Delcare Q-Learning Agent
    agent = Agent(epsilon, discount, Learning_rate)

    # Training Hyperparameters (Tweak These)
    num_episodes = 20000

    # Train the Q-Learning Agent
    train(agent, num_episodes)

    # Save the Agents Q-Table
    agent.saveQ()