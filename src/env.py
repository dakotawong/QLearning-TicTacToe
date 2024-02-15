#from agent import Agent

# TicTacToe Game Class
class TicTacToe():

    """
    Agent: the Q-Learning Agent.
    Opponent: opposition that will play against the Agent.
    Board: 2D List that repesents the game state.
    """
    def __init__(self, agent, opponent = None):
        # Initialize the game board (* means empty square)
        self.board = [
            ["*", "*", "*"],
            ["*", "*", "*"],
            ["*", "*", "*"],
        ]
        # Q-Learning Agent
        self.agent = agent
        # Agent Opponent (set to None to play the Agent yourself)
        self.opponent = opponent

    # Function to check if symbol won (Returns True | false)
    def isWinner(self, symbol):
        # Check rows and columns
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == symbol:
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] == symbol:
                return True
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == symbol:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == symbol:
            return True
        # No winner
        return False
    
    # Checks for a Draw (Returns True | false)
    def isDraw(self):
        for row in self.board:
            for val in row:
                if val == "*":
                    return False
        return True

    # Function to get state as string (hashable representation of state)
    def getStateString(self):
        state_string = ""
        for row in self.board:
            for val in row:
                state_string += val
        return state_string

    # Function to get list of possible next actions
    def possibleActions(self):
        actions = []
        for i in range(3):
            for j in range(3):
                if (self.board[i][j] == "*"):
                    actions.append([i, j])
        return actions

    # Function to Print the Board
    def printBoard(self):
        print("\n")
        print(f"  {self.board[0][0]} | {self.board[0][1]} | {self.board[0][2]}")
        print(" -----------")
        print(f"  {self.board[1][0]} | {self.board[1][1]} | {self.board[1][2]}")
        print(" -----------")
        print(f"  {self.board[2][0]} | {self.board[2][1]} | {self.board[2][2]}")
        print("\n")

    # Function to execute an actions
    def executeAction(self, move, character):
        self.board[move[0]][move[1]] = character

    # Function to take an opponent turn (get action and execute action)
    def OpponentTurn(self):
        # Check if there is an opponent (Human or Agent)
        if (self.opponent == None):
            # No Opponent - Take Moves from Standard Input (Human)
            self.printBoard()
            possible_actions = self.possibleActions()
            while True:
                try:
                    input_str = input("Enter the row and column numbers (separated by a space): ")
                    action = list(map(int, input_str.split()))
                    if action in possible_actions:
                        self.executeAction(action, "O")
                        return
                    else:
                        print("Invalid input. Please enter two numbers separated by a space (eg. '0 1').")
                except ValueError:
                    print("Invalid input. Please enter two numbers separated by a space (eg. '0 1').")
        else:
            # Get Move from the Opponent (another Agent)
            state = self.getStateString()
            action = self.opponent.getAction(state)
            self.executeAction(action, "O")

    # Function to reset board state for new game
    def reset(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = "*"
        return

    # Function to play a game of TicTacToe
    def playGame(self):
        # Reset the Game Board (State)
        self.reset()
        # Get Agent Move
        state = self.getStateString()
        action = self.agent.getAction(state)

        # GAME LOOP
        while True:
            # Get agent move
            action = self.agent.getAction(state)
            # Execute agent move
            self.executeAction(action, "X")

            # Check Agent Won (Break if Over)
            if (self.isWinner("X")):
                # Reward for Win
                reward = 1
                break
            # Check for Draw (Break if Over)
            if (self.isDraw()):
                # Reward for Draw
                reward = 0
                break;
            # Default Reward
            reward = 0

            # Take opponent's turn (get action and execute it)
            self.OpponentTurn()

            # Check Opponent Won (Break if Over)
            if (self.isWinner("O")):
                # Reward for Agent Loss
                reward = -1
                break

            # Get the Next Game State
            next_state = self.getStateString()
            # Update Agent 
            self.agent.update(next_state, action, reward, state)
            # Update State (state = next_state)
            state = next_state

        # Update Agent on Exit 
        self.agent.update(None, action, reward, state)

        # Return 1 for Agent win and -1 for Agent Loss
        return reward
