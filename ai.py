import random
import minimax_tictactoe

NUMBER_OF_ROWS = 3
EMPTY_SPACE = "-"


def random_ai(board, player):
        """Randomly selects a move."""
        row = random.randint(0, NUMBER_OF_ROWS - 1)
        column = random.randint(0, NUMBER_OF_ROWS - 1)
        while board[row][column] != EMPTY_SPACE:
            row = random.randint(0, NUMBER_OF_ROWS - 1)
            column = random.randint(0, NUMBER_OF_ROWS - 1)
        return (row, column)


def find_winning_moves_ai(board, player):
    """If the current player can win, returns winning move. Otherwise, returns a random move."""
    move = find_winning_moves(board, player, True)
    if move != -1:
        return move
    return random_ai(board, player)


def find_winning_and_losing_moves_ai(board, player):
    """If the current player can win, returns winning move. If the current player can block the
    opponent from winning, then returns that move. Otherwise, returns a random move."""
    move = find_winning_moves(board, player, True)
    if move != -1:
        return move
    move = find_winning_moves(board, player, False)
    if move != -1:
        return move
    return random_ai(board, player)


def find_winning_moves(board, player, win):
    """Returns a winning move (win), or a way to block a losing move (not win) if one exists.
    Otherwise, returns -1."""
    moves = []
    winning_moves = []
    moves.append(check_rows(board, player, win))
    moves.append(check_columns(board, player, win))
    moves.append(check_diagonals(board, player, win))
    
    for move in moves:
        if move != -1:
            winning_moves.append(move)
    
    if len(winning_moves) > 0:
        return random.choice(winning_moves)
    return -1


def check_rows(board, player, win):
    """ Checks every row to see if there is a winning move or way to block a winning move.
    Returns -1 if there isn't a winning move."""
    for r in range(NUMBER_OF_ROWS):
        score = 0
        current_move = ()
        for c in range(NUMBER_OF_ROWS):
            if board[r][c] == "X":
                score += 1
            elif board[r][c] == "O":
                score -= 1
            else:
                current_move = (r, c)

        if current_move != () and (score == 2 or score == -2):
            if ((win and player == "X" and score == 2) 
            or (win and player == "O" and score == -2)
            or (not win and player == "X" and score == -2)
            or (not win and player == "O" and score == 2)):
                return current_move
    return -1


def check_columns(board, player, win):
    """ Checks every column to see if there is a winning move or way to block a winning move.
    Returns -1 if there isn't a winning move."""
    for c in range(NUMBER_OF_ROWS):
        score = 0
        current_move = ()
        for r in range(NUMBER_OF_ROWS):
            if board[r][c] == "X":
                score += 1
            elif board[r][c] == "O":
                score -= 1
            else:
                current_move = (r, c)

        if current_move != () and (score == 2 or score == -2):
            if ((win and player == "X" and score == 2) 
            or (win and player == "O" and score == -2)
            or (not win and player == "X" and score == -2)
            or (not win and player == "O" and score == 2)):
                return current_move
    return -1


def check_left_diagonal(board, player, win):
    """ Checks left diagonal to see if there is a winning move or way to block a winning move.
    Returns -1 if there isn't a winning move."""
    score = 0
    current_move = ()
    for r in range(NUMBER_OF_ROWS):
        if board[r][r] == "X":
            score += 1
        elif board[r][r] == "O":
            score -= 1
        else:
            current_move = (r, r)
        if current_move != () and (score == 2 or score == -2):
            if ((win and player == "X" and score == 2) 
            or (win and player == "O" and score == -2)
            or (not win and player == "X" and score == -2)
            or (not win and player == "O" and score == 2)):
                return current_move
    return -1


def check_right_diagonal(board, player, win):
    """ Checks right diagonal to see if there is a winning move or way to block a winning move.
    Returns -1 if there isn't a winning move."""
    r = NUMBER_OF_ROWS - 1
    score = 0
    current_move = ()
    for c in range(NUMBER_OF_ROWS):
        if board[r][c] == "X":
            score += 1
        elif board[r][c] == "O":
            score -= 1
        else:
            current_move = (r, c)
        if current_move != () and (score == 2 or score == -2):
            if ((win and player == "X" and score == 2) 
            or (win and player == "O" and score == -2)
            or (not win and player == "X" and score == -2)
            or (not win and player == "O" and score == 2)):
                return current_move
        r -= 1
    return -1


def check_diagonals(board, player, win):
    """ Checks diagonals to see if there is a winning move or way to block a winning move.
    Returns -1 if there isn't a winning move."""
    moves = []
    winning_moves = []
    moves.append(check_left_diagonal(board, player, win))
    moves.append(check_right_diagonal(board, player, win))
    
    for move in moves:
        if move != -1:
            winning_moves.append(move)
    
    if len(winning_moves) > 0:
        return random.choice(winning_moves)
    return -1


def minimax_ai(board, player):
        """Returns the next move determined by the minimax ai which compares all possible moves for the best
        possible score."""
        minimax = minimax_tictactoe.MiniMax_TicTacToe(board)
        return minimax.get_minimax_move(player)