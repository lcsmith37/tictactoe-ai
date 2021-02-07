import tictactoe

t = tictactoe.TicTacToe()


number_of_turns = 0
x_player = input("Specify an AI for X:\n[1] human_player\n[2] random_ai\n[3] find_winning_moves_ai\n[4] find_winning_and_losing_moves_ai\n[5] minimax_ai\n")
o_player = input("Specify an AI for O:\n[1] human_player\n[2] random_ai\n[3] find_winning_moves_ai\n[4] find_winning_and_losing_moves_ai\n[5] minimax_ai\n")

t.print_board()

while not t.game_over():
    move = ()
    print()
    if number_of_turns % 2 == 0:
        print("X's turn!")
        player = "X"
        move = t.get_move(x_player, player)
    else:
        print("O's turn!")
        player = "O"
        move = t.get_move(o_player, player)
    
    t.update_board(move[0], move[1], player)

    t.print_board()

    number_of_turns += 1


if t.is_win() != "null":
    print(t.is_win(), "wins!")
else:
    print("Tie!")



