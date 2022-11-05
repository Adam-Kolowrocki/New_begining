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
    print(f'Game is for two players, You can chose "O" or "X".')
    print(f'It is not needed to use capital letters.')
    input(f'Press any key to continue...')
    player_names()


def player_names():
    pass


def table_print():
    print(f'OX')


if __name__ == "__main__":
    main()
