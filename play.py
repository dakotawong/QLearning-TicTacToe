from src.agent import Agent 
from src.env import TicTacToe

"""
This file can be used to play against the Q-Learning Agent. 
"""

def play(agent):

    # Declare the training environment (no opponent means human opponent)
    env = TicTacToe(agent)

    # Store testing metrics
    wins, losses, ties = 0, 0, 0

    # Agent now trains acrosses specified number of episodes
    while True:
        # Play game and get final reward (win = 1 , loss = -1, tie = 0)
        reward = env.playGame()

        # Print Board
        env.printBoard()

        # Update metrics
        if (reward == 1):
            print("Agent Wins")
            losses += 1
        elif (reward == -1):
            print("Agent Loses")
            wins += 1
        elif(reward == 0):
            print("Ties")
            ties += 1

        # Ask player to continue playing
        cont = input("Keep playing (y/n): ")
        if (cont.lower() == 'y'):
            continue
        break

    # Print Metrics
    print("Your Stats:")
    print(f"Wins: {wins}, Losses: {losses}, Ties: {ties}")


if __name__ == "__main__":

    # Set epsilon = 0 to pick always pick best action (greedy)
    epsilon = 0

    # Set learning rate to 0 to prevent training
    learning_rate = 0

    # Delcare Q-Learning Agent
    agent = Agent(epsilon=epsilon, learning_rate=learning_rate)

    # load the saved Q-Table
    agent.loadQ()

    # Play the Q-Learning Agent
    play(agent)
