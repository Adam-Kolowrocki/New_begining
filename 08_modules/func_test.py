def main():
    print_result(get_data())


def get_data():
    user_num = int(input(f'Type a number ->'))
    return user_num


def absolut_value(num):
    if num >= 0:
        return num
    else:
        return -num


def print_result(absolut):
    print(absolut_value(absolut))


if __name__ == "__main__":
    main()
