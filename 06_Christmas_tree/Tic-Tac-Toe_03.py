table = [
    [' ', '1', ' ', '2', ' ', '3'],
    ['A', '.', '|', '.', '|', '.'],
    ['B', '.', '|', '.', '|', '.'],
    ['C', '.', '|', '.', '|', '.'],
]
moves = {'a1': [1, 1], 'a2': [1, 3], 'a3': [1, 5], 'b1': [2, 1], 'b2': [2, 3], 'b3': [2, 5], 'c1': [3, 1],
         'c2': [3, 3], 'c3': [3, 5]}


def main():
    """Start function of the game"""
    print(f'Lets play "Tic Tac Toe" game.\n')
    print_table(table)
    print(f'\nIt is not needed to use capital letters.')
    input(f'Press ENTER to continue...')
    player_x, player_o = player_names()
    main_game(player_x, player_o)


def print_table(game_table):
    """Prints empty Tic Tac Toe table."""
    for i in range(len(game_table)):
        for j in range(len(game_table[i])):
            print(game_table[i][j], end=' ')
        print()


def player_names():
    """Collect Players names"""
    player_x = input(f'Type player X name -> ')
    player_o = input(f'Type player O name -> ')
    return player_x, player_o


def main_game(player_x, player_o):
    while True:
        ttt_game(player_x, 'X', player_x, player_o)
        ttt_game(player_o, 'O', player_x, player_o)


def ttt_game(player_name, sign, player_x, player_o):
    """The game function"""
    move = get_move(player_name)
    if if_move_possible(table, move):
        add_to_table(table, move, sign, player_name, player_x, player_o)
    else:
        ttt_game(player_name, sign, player_x, player_o)


def get_move(player):
    while True:
        player_move = input(f'Player {player}, what is Your move -> ')
        if player_move in moves:
            print(f'Player {player} mark position {player_move.upper()}')
            return moves[player_move.lower()]


def if_move_possible(game_table, move):
    """Check if move possible"""
    if game_table[move[0]][move[1]] == '.':
        return True
    else:
        print(f'This move is not allowed...')
        return False


def add_to_table(game_table, move, sign, player_name, player_x, player_o):
    game_table[move[0]][move[1]] = sign
    print_table(game_table)
    game_result(sign, player_name, player_x, player_o)


def game_result(sign, player, player_x, player_o):
    """Checks who won the game"""
    if (table[1][1] == sign and table[1][3] == sign and table[1][5] == sign) or \
            (table[2][1] == sign and table[2][3] == sign and table[2][5] == sign) or \
            (table[3][1] == sign and table[3][3] == sign and table[3][5] == sign) or \
            (table[1][1] == sign and table[2][1] == sign and table[3][1] == sign) or \
            (table[1][3] == sign and table[2][3] == sign and table[3][3] == sign) or \
            (table[1][5] == sign and table[2][5] == sign and table[3][5] == sign) or \
            (table[1][1] == sign and table[2][3] == sign and table[3][5] == sign) or \
            (table[1][5] == sign and table[2][3] == sign and table[3][1] == sign):
        print(f'***{player.upper()}*** WON THE GAME !!!')
        decision(player_x, player_o)
    elif '.' in table[1] or '.' in table[2] or '.' in table[3]:
        return
    else:
        print(f'Draw')
        decision(player_x, player_o)


def decision(player_x, player_o):
    while True:
        end_decision = input(f'Would you like to continue? [yes/no]: ')
        if end_decision in ['y', 'n']:
            if end_decision == 'y':
                for i in range(1, 4):
                    for j in range(1, 7, 2):
                        table[i][j] = '.'
                main_game(player_x, player_o)
            else:
                print(f'Game Over')
                return False


if __name__ == "__main__":
    main()
