moves = {'a1': [1, 1], 'a2': [1, 3], 'a3': [1, 5], 'b1': [2, 1], 'b2': [2, 3], 'b3': [2, 5], 'c1': [3, 1],
         'c2': [3, 3], 'c3': [3, 5]}

player_move = input(f'Player, what is Your move -> ')
print(player_move)
print(type(player_move))
if player_move[0].isdigit():
    player_move = player_move[1] + player_move[0]
print(player_move)
print(type(player_move))
if player_move in moves:
    print(f'Player mark position {player_move.upper()}')






# def player_names():
#     """Collect Players names"""
#     player_x = input(f'Type player X name -> ')
#     player_o = input(f'Type player O name -> ')
#     return player_x, player_o
#
#
# player_x, player_o = player_names()
#
# print(f'Gracz X - {player_x}')
# print(f'Grac O - {player_o}')


    # player_x_move = get_move(player_x)
    # table_print(table, player_x, player_x_move, 'X')
    # player_o_move = get_move(player_o)
    # table_print(table, player_o, player_o_move, 'O')






# table = [
#     [' ', '1', ' ', '2', ' ', '3'],
#     ['A', '.', '|', '.', '|', '.'],
#     ['B', '.', '|', '.', '|', '.'],
#     ['C', '.', '|', '.', '|', '.'],
# ]
#
#
# def table_print(table, name, move, sign):
#     """Print game table"""
#     if move[0] == 'a' and move[1] == '1':
#         if table[1][1] == '.':
#             table[1][1] = sign
#         else:
#             print(f'This move is not allowed...')
#             get_move(name)
#     elif move[0] == 'a' and move[1] == '2':
#         if table[1][3] == '.':
#             table[1][3] = sign
#         else:
#             print(f'This move is not allowed...')
#             get_move(name)
#     elif move[0] == 'a' and move[1] == '3':
#         if table[1][5] == '.':
#             table[1][5] = sign
#         else:
#             print(f'This move is not allowed...')
#             get_move(name)
#     elif move[0] == 'b' and move[1] == '1':
#         if table[2][1] == '.':
#             table[2][1] = sign
#         else:
#             print(f'This move is not allowed...')
#             get_move(name)
#     elif move[0] == 'b' and move[1] == '2':
#         if table[2][3] == '.':
#             table[2][3] = sign
#         else:
#             print(f'This move is not allowed...')
#             get_move(name)
#     elif move[0] == 'b' and move[1] == '3':
#         if table[2][5] == '.':
#             table[2][5] = sign
#         else:
#             print(f'This move is not allowed...')
#             get_move(name)
#     elif move[0] == 'c' and move[1] == '1':
#         if table[3][1] == '.':
#             table[3][1] = sign
#         else:
#             print(f'This move is not allowed...')
#             get_move(name)
#     elif move[0] == 'c' and move[1] == '2':
#         if table[3][3] == '.':
#             table[3][3] = sign
#         else:
#             print(f'This move is not allowed...')
#             get_move(name)
#     elif move[0] == 'c' and move[1] == '3':
#         if table[3][5] == '.':
#             table[3][5] = sign
#         else:
#             print(f'This move is not allowed...')
#             get_move(name)
#
#     for i in range(len(table)):
#         for j in range(len(table[i])):
#             print(table[i][j], end=' ')
#         print()
#     return table
#
#
# table_print(table, 'Adam', 'a1', 'X')
