# Stwórz moduł, który przechowuje wzór na deltę.
# Skorzystaj z wbudowanego modułu math. W nowym pliku wykorzystaj moduł.
import delta


def main():
    a, b, c = user_data()
    print(f'Delta od a={a}, b={b} i c={c} wynosi {delta.delta(a, b, c)}')


def user_data():
    print(f'Funkcja oblicza deltę od "a", "b", i "c".')
    a = int(input(f'podaj długość boku a -> '))
    b = int(input(f'podaj długość boku b -> '))
    c = int(input(f'podaj długość boku c -> '))
    return a, b, c


if __name__ == "__main__":
    main()
