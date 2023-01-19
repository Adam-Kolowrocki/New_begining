# try:
#     x = 5 / 0
# except ArithmeticError:
#     print(f'ArithmeticError')
# except TypeError as t:
#     print(t)
# except TabError as tt:
#     print(tt)
# finally:
#     print(f'I will always be in this place...')
import sys
try:
    5 / 0
except Exception:
    print("Błąd to: ", sys.exc_info()[0])
# raise KeyboardInterrupt
# raise ValueError
# raise MemoryError('Cokolwiek')
# print('Początek')
# raise Exception('Błąd')
# print(f'Koniec')


def predict_future():
    num = int(input("Podaj dowolną liczbę naturalną: "))
    if num < 0:
        raise ValueError("To nie jest liczba naturalna!")
    else:
        print("Za", 10 * num, "ludzkość będzie mogła się teleportować")


try:
    predict_future()
except ValueError as e:
    print(e)
