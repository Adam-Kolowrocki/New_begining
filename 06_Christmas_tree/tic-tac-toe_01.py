# Write a tic-tac-toe game for two players. Start from the most important - play.
# Then add menu, options like player names and Your ideas.
# The game could look like that:
#
#    1   2   3
# A  . | . | .
# B  . | . | .
# C  . | . | .
#
# Player X, mark position: A1
#
#    1   2   3
# A  X | . | .
# B  . | . | .
# C  . | . | .
#
# Player O, mark position: B2
#
#    1   2   3
# A  X | . | .
# B  . | O | .
# C  . | . | .
#
# Player X, mark position: B1
#
# ...
#
#    1   2   3
# A  X | O | X
# B  X | O | X
# C  O | X | O
#
# Draw!
#
# Would you like to continue? [yes/no]:

# Advice - do not start from display. Empty fixed table is not a problem.
# Plan the play creating algorithm schema of necessary steps.


def main():
    """Main function of the game"""
    print(f'Lets play "Tic Tac Toe" game.\n')
    print('   1   2   3\n'
          'A  . | . | .\n'
          'B  . | . | .\n'
          'C  . | . | .\n')

    print(f'It is not needed to use capital letters.')
    input(f'Press any key to continue...')


def player_names(player):
    player_name = input(f'Type {player} name -> ')
    return player_name


def table_print(move, sign):
    # move = a1
    print('   1   2   3\n'
          'A  . | . | .\n'
          'B  . | . | .\n'
          'C  . | . | .\n')


moves = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']


def get_move(player):
    while True:
        player_move = input(f'Player {player}, what is Your move -> ')
        if player_move in moves:
            print(f'Player {player} mark position {player_move.upper()}')
            return player_move.lower()


if __name__ == "__main__":
    main()

player_x = player_names('Player X')
player_o = player_names('Player O')
while True:
    player_x_move = get_move(player_x)
    table_print(player_x_move, 'X')
    player_o_move = get_move(player_o)
    table_print(player_o_move, 'O')
