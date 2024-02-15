from src.agent import Agent 
from src.env import TicTacToe

"""
This file can be used to Test the win percentaghe of
the Q-Learning Agent against another agent. 
"""

def test(agent, num_episodes):

    # Declare opponent to train agent against (Epsilon of 1 makes the agent pick actions randomly)
    opponent = Agent(epsilon=1)

    # Declare the training environment
    env = TicTacToe(agent, opponent)

    # Store testing metrics
    wins, losses, ties = 0, 0, 0

    # Agent now trains acrosses specified number of episodes
    print("Testing...")
    for i in range(num_episodes):
        # Play game and get resuts (win = 1 , loss = -1, tie = 0)
        res = env.playGame()
        # Update metrics
        if res == 1:
            wins += 1
        elif res == -1:
            losses += 1
        else:
            ties += 1
    
    # Print Metrics
    print(f"Wins: {wins}, Losses: {losses}, Ties: {ties}")

    # Training Complete
    print("Testing Complete")


if __name__ == "__main__":

    # Set epsilon = 0 to pick always pick best action (greedy)
    epsilon = 0

    # Set learning rate to 0 to prevent training
    learning_rate = 0

    # Delcare Q-Learning Agent
    agent = Agent(epsilon=epsilon, learning_rate=learning_rate)

    # load the saved Q-Table
    agent.loadQ()

    # Number of games in test (Tweak This)
    num_episodes = 1000

    # Test the Q-Learning Agent
    test(agent, num_episodes)
