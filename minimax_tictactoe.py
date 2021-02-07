import tictactoe

NUMBER_OF_ROWS = 3
EMPTY_SPACE = "-"


class MiniMax_TicTacToe:

    def __init__(self, board):
        """Constructor for the TicTacToe class."""
        self.board = board
        self.best_scores = {}
        self.best_moves = {}


    def minimax_score(self, new_board, maximize, player, depth):
        """Returns the best score possible from the given board. Updates the best_scores and best_moves
        dictionaries after the best score is determined."""
        result = self.board_full(new_board)
        # base case: game is over
        if result != -1:
            if result == "X":
                return 10
            elif result == "O":
                return -10
            else:
                return 0

        best_move = None
        best_score = 1000
        next_player = "X"
        if (player == "X"):
            next_player = "O"
            best_score = -1000

        for r in range(NUMBER_OF_ROWS):
            for c in range(NUMBER_OF_ROWS):
                if new_board[r][c] == EMPTY_SPACE:
                    # Used as key for self.best_moves
                    first_board_string = self.get_string_representation(new_board)
                    new_board[r][c] = player
                    # Used as key for self.best_scores
                    board_string = self.get_string_representation(new_board)
                    if self.best_scores.get(best_move) != None:
                        return self.best_scores.get(best_move)

                    # If best_score hasn't been found for the current board:
                    score = self.minimax_score(new_board, not maximize, next_player, depth + 1)
                    new_board[r][c] = EMPTY_SPACE
                    if maximize and best_score < score:
                        best_score = score
                        best_move = (r, c)
                    elif not maximize and best_score > score:
                        best_score = score
                        best_move = (r, c)
                        
        self.best_scores.update({board_string: best_score})
        self.best_moves.update({first_board_string: best_move})
        return best_score


    def get_minimax_move(self, player):
        """Returns the next move using the minimax ai. Returns the move with the best possible score."""
        maximize = False
        if player == "X":
            maximize = True
        self.minimax_score(self.board, maximize, player, 1)
        return self.best_moves.get(self.get_string_representation(self.board))


    def board_full(self, current_board):
        """Returns -1 if the board is not full. Otherwise, returns "X", "O", or "tie" depending on the
        result."""
        for i in range(NUMBER_OF_ROWS):
            if current_board[i][0] != EMPTY_SPACE and current_board[i][0] == current_board[i][1] == current_board[i][2]:
                return current_board[i][0]
            if current_board[0][i] != EMPTY_SPACE and current_board[0][i] == current_board[1][i] == current_board[2][i]:
                return current_board[0][i]
        if current_board[0][0] != EMPTY_SPACE and current_board[0][0] == current_board[1][1] == current_board[2][2]:
            return current_board[0][0]
        if current_board[0][2] != EMPTY_SPACE and current_board[0][2] == current_board[1][1] == current_board[2][0]:
            return current_board[0][2]

        for r in range(NUMBER_OF_ROWS):
            for c in range(NUMBER_OF_ROWS):
                if current_board[r][c] == EMPTY_SPACE:
                    return -1
        return "tie"


    def get_string_representation(self, new_board):
        """Returns a string representation of the specified board."""
        result = ""
        for r in range(NUMBER_OF_ROWS):
            for c in range(NUMBER_OF_ROWS):
                result += new_board[r][c]
        return result

        





    