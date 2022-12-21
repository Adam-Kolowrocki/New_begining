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
table = [
    [' ', '1', ' ', '2', ' ', '3'],
    ['A', '.', '|', '.', '|', '.'],
    ['B', '.', '|', '.', '|', '.'],
    ['C', '.', '|', '.', '|', '.'],
]
moves = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']


def main():
    """Main function of the game"""
    print(f'Lets play "Tic Tac Toe" game.\n')
    table_print(table, '0', '0', '0')
    print(f'\nIt is not needed to use capital letters.')
    input(f'Press ENTER to continue...')


def player_names():
    """Collect Players names"""
    player_x = input(f'Type player X name -> ')
    player_o = input(f'Type player O name -> ')
    return player_x, player_o


def table_print(table, name, move, sign):
    """Print game table"""
    if move[0] == 'a' and move[1] == '1':
        if table[1][1] == '.':
            table[1][1] = sign
        else:
            print(f'This move is not allowed...')
            get_move(name)
    elif move[0] == 'a' and move[1] == '2':
        if table[1][3] == '.':
            table[1][3] = sign
        else:
            print(f'This move is not allowed...')
            get_move(name)
    elif move[0] == 'a' and move[1] == '3':
        if table[1][5] == '.':
            table[1][5] = sign
        else:
            print(f'This move is not allowed...')
            get_move(name)
    elif move[0] == 'b' and move[1] == '1':
        if table[2][1] == '.':
            table[2][1] = sign
        else:
            print(f'This move is not allowed...')
            get_move(name)
    elif move[0] == 'b' and move[1] == '2':
        if table[2][3] == '.':
            table[2][3] = sign
        else:
            print(f'This move is not allowed...')
            get_move(name)
    elif move[0] == 'b' and move[1] == '3':
        if table[2][5] == '.':
            table[2][5] = sign
        else:
            print(f'This move is not allowed...')
            get_move(name)
    elif move[0] == 'c' and move[1] == '1':
        if table[3][1] == '.':
            table[3][1] = sign
        else:
            print(f'This move is not allowed...')
            get_move(name)
    elif move[0] == 'c' and move[1] == '2':
        if table[3][3] == '.':
            table[3][3] = sign
        else:
            print(f'This move is not allowed...')
            get_move(name)
    elif move[0] == 'c' and move[1] == '3':
        if table[3][5] == '.':
            table[3][5] = sign
        else:
            print(f'This move is not allowed...')
            get_move(name)

    for i in range(len(table)):
        for j in range(len(table[i])):
            print(table[i][j], end=' ')
        print()
    return table


def get_move(player):
    while True:
        player_move = input(f'Player {player}, what is Your move -> ')
        if player_move in moves:
            print(f'Player {player} mark position {player_move.upper()}')
            return player_move.lower()


def game_result(sign):
    """Checks who won the game"""
    if (table[1][1] == sign and table[1][3] == sign and table[1][5] == sign) or \
            (table[2][1] == sign and table[2][3] == sign and table[2][5] == sign) or \
            (table[3][1] == sign and table[3][3] == sign and table[3][5] == sign) or \
            (table[1][1] == sign and table[2][1] == sign and table[3][1] == sign) or \
            (table[1][3] == sign and table[2][3] == sign and table[3][3] == sign) or \
            (table[1][5] == sign and table[2][5] == sign and table[3][5] == sign) or \
            (table[1][1] == sign and table[2][3] == sign and table[3][5] == sign) or \
            (table[1][5] == sign and table[2][3] == sign and table[3][1] == sign):
        print(f'Player {sign} - - WON THE GAME !!!')


if __name__ == "__main__":
    main()

player_x, player_o = player_names()
while True:
    player_x_move = get_move(player_x)
    table_print(table, player_x, player_x_move, 'X')
    player_o_move = get_move(player_o)
    table_print(table, player_o, player_o_move, 'O')
