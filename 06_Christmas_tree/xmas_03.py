#     *
#    /|\
#   /_|_\
#    /|\
#   / | \
#  /__|__\
#    /|\
#   / | \
#  /  |  \
# /___|___\
#     |

def main():
    n = int(input('Choose size of the Christmas tree:'))
    print_tree(n)


def print_segment(m, total_width):
    for size in range(3, m + 1, 2):
        line = ((('/' + ((size // 2) - 1) * ' ') + '|' + ((size // 2) - 1) * ' ') + '\\')
        l_line = ((('/' + ((size // 2) - 1) * '_') + '|' + ((size // 2) - 1) * '_') + '\\')
        if size < m:
            print(line.center(total_width))
        else:
            print(l_line.center(total_width))


def print_tree(size):
    print('*'.center(size))
    for i in range(5, size + 1, 2):
        print_segment(i, size)
    print('|'.center(size))


if __name__ == '__main__':
    main()
