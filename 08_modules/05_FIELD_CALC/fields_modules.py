import math


def main():
    """Main function"""
    print(f'This script calculate field of different figures')


def triangle(a, h):
    return (a * h) / 2


def square(a):
    return a ** 2


def rectangle(a, b):
    return a * b


def diamond(a, h):
    return a * h


def trapeze(a, b, h):
    return ((a + b) * h) / 2


def hexagon(a):
    return 6 * (((a ** 2) * math.isqrt(3)) / 4)


def octagon(a):
    return 2 * (a + math.isqrt(2) * (a ** 2))


if __name__ == "__main__":
    main()
