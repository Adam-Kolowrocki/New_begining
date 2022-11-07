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


def main():
    """Main function of the game"""
    print(f'Lets play "Tic Tac Toe" game.\n')
    table_print(table, '0', '0')
    print(f'\nIt is not needed to use capital letters.')
    input(f'Press any key to continue...')


def player_names(player):
    player_name = input(f'Type {player} name -> ')
    return player_name


def table_print(table, move, sign):
    if move[0] == 'a' and move[1] == '1':
        if table[1][1] == '.':
            table[1][1] = sign
        else:
            print(f'This move is not allowed...')
            # get_move(sign)
    elif move[0] == 'a' and move[1] == '2':
        if table[1][3] == '.':
            table[1][3] = sign
        else:
            print(f'This move is not allowed...')
            get_move(sign)
    elif move[0] == 'a' and move[1] == '3':
        if table[1][5] == '.':
            table[1][5] = sign
        else:
            print(f'This move is not allowed...')
            get_move(sign)
    elif move[0] == 'b' and move[1] == '1':
        if table[2][1] == '.':
            table[2][1] = sign
        else:
            print(f'This move is not allowed...')
            get_move(sign)
    elif move[0] == 'b' and move[1] == '2':
        if table[2][3] == '.':
            table[2][3] = sign
        else:
            print(f'This move is not allowed...')
            get_move(sign)
    elif move[0] == 'b' and move[1] == '3':
        if table[2][5] == '.':
            table[2][5] = sign
        else:
            print(f'This move is not allowed...')
            get_move(sign)
    elif move[0] == 'c' and move[1] == '1':
        if table[3][1] == '.':
            table[3][1] = sign
        else:
            print(f'This move is not allowed...')
            get_move(sign)
    elif move[0] == 'c' and move[1] == '2':
        if table[3][3] == '.':
            table[3][3] = sign
        else:
            print(f'This move is not allowed...')
            get_move(sign)
    elif move[0] == 'c' and move[1] == '3':
        if table[3][5] == '.':
            table[3][5] = sign
        else:
            print(f'This move is not allowed...')
            get_move(sign)

    for i in range(len(table)):
        for j in range(len(table[i])):
            print(table[i][j], end=' ')
        print()
    return table


moves = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']


def get_move(player):
    while True:
        player_move = input(f'Player {player}, what is Your move -> ')
        if player_move in moves:
            print(f'Player {player} mark position {player_move.upper()}')
            return player_move.lower()


table = [
    [' ', '1', ' ', '2', ' ', '3'],
    ['A', '.', '|', '.', '|', '.'],
    ['B', '.', '|', '.', '|', '.'],
    ['C', '.', '|', '.', '|', '.'],
]


def game_result():
    table_print(table, '0', '0')
    if (table[1][1] == 'X' and table[1][3] == 'X' and table[1][5] == 'X') or (
            table[2][1] == 'X' and table[2][3] == 'X' and table[2][5] == 'X') or (
            table[3][1] == 'X' and table[3][3] == 'X'
            and table[3][5] == 'X') or (table[1][1] == 'X' and table[2][1] == 'X' and table[3][1] == 'X') or (
            table[1][3] == 'X' and table[2][3] == 'X' and table[3][3] == 'X') or (table[1][5] == 'X'
                                                                                  and table[2][5] == 'X' and table[3][
                                                                                      5] == 'X') or (
            table[1][1] == 'X' and table[2][3] == 'X'
            and table[3][5] == 'X') or (table[1][5] == 'X' and table[2][3] == 'X' and table[3][1] == 'X'):
        print(f'Player X - {player_x} WON THE GAME !!!')


if __name__ == "__main__":
    main()

player_x = player_names('Player X')
player_o = player_names('Player O')

if '.' not in table[1] and '.' not in table[2] and '.' not in table[3]:
    game_result()

while True:
    player_x_move = get_move(player_x)
    table_print(table, player_x_move, 'X')
    player_o_move = get_move(player_o)
    table_print(table, player_o_move, 'O')
