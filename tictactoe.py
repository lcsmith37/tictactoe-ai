import ai

NUMBER_OF_ROWS = 3
EMPTY_SPACE = "-"


class TicTacToe:


    def __init__(self):
        """Constructor for the TicTacToe class."""
        self.board = [[EMPTY_SPACE, EMPTY_SPACE, EMPTY_SPACE],
                      [EMPTY_SPACE, EMPTY_SPACE, EMPTY_SPACE], 
                      [EMPTY_SPACE, EMPTY_SPACE, EMPTY_SPACE]]


    def human_player(self, player):
        """Gets a player's move from user input. Returns a tuple (row, column)."""
        row = self.get_row()
        column = self.get_column()
        while not self.is_valid_move(row, column):
            print("That spot is already taken! Choose a different location.")
            row = self.get_row()
            column = self.get_column()
        return (row, column)


    def get_row(self):
        """Gets and returns a valid row number."""
        row = int(input("Enter row: "))
        while row < 0 or row >= 3:
            row = int(input("The row number must be between 0 and 2. \nEnter row: "))
        return row


    def get_column(self):
        """Gets and returns a valid column number."""
        column = int(input("Enter column: "))
        while column < 0 or column >= 3:
            column = int(input("The column number must be between 0 and 2. \nEnter column: "))
        return column

    
    def get_move(self, ai_choice, player):
        """Gets the move using the specified ai type. If the ai number is not any of specified options,
        a move from random_ai is returned."""
        if ai_choice == "1":
            return self.human_player(player)
        elif ai_choice == "2":
            return ai.random_ai(self.board, player)
        elif ai_choice == "3":
            return ai.find_winning_moves_ai(self.board, player)
        elif ai_choice == "4":
            return ai.find_winning_and_losing_moves_ai(self.board, player)
        elif ai_choice == "5":
            return ai.minimax_ai(self.board, player)
        return ai.random_ai(self.board, player)


    def is_valid_move(self, row, column):
        """Returns if the given row and column correspond to a valid move."""
        if row >= NUMBER_OF_ROWS or column >= NUMBER_OF_ROWS:
            return False
        return self.board[row][column] == EMPTY_SPACE


    def update_board(self, row, column, char):
        """Updates the board with the specified move and removes that move from the valid_moves list."""
        self.board[row][column] = char

    
    def is_win(self):
        """Returns the winner if there is one. Otherwise, returns null."""
        for i in range(NUMBER_OF_ROWS):
            if self.board[i][0] != EMPTY_SPACE and self.board[i][0] == self.board[i][1] == self.board[i][2]:
                return self.board[i][0]
            if self.board[0][i] != EMPTY_SPACE and self.board[0][i] == self.board[1][i] == self.board[2][i]:
                return self.board[0][i]
        if self.board[0][0] != EMPTY_SPACE and self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return self.board[0][0]
        if self.board[0][2] != EMPTY_SPACE and self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return self.board[0][2]
        return "null"


    def game_over(self):
        """Returns if the game is over."""
        if self.is_win() != "null":
            return True
        for i in range(NUMBER_OF_ROWS):
            for j in range (NUMBER_OF_ROWS):
                if self.board[i][j] == EMPTY_SPACE:
                    return False
        return True


    def print_board(self):
        """Prints the current board."""
        print("    0", "1", "2")
        print("   -------")
        for i in range(NUMBER_OF_ROWS):
            print(i, "|", self.board[i][0], self.board[i][1], self.board[i][2])
