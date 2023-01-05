# Stwórz moduł, który dla dowolnej wartości n, zwróci ciąg Fibonacciego
def main():
    print(f'Script returns Fibonacci sequence for given n number.')
    print(fibonacci(user_number()))


def user_number():
    user_n = int(input(f'For what "n" numer do You want to receive Fibonacci sequence -> '))
    return user_n


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    main()
