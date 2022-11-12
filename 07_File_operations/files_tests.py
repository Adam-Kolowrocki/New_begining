with open('/home/adam/Dokumenty/Python-Kurs/Files/inwokacja.txt', 'r', encoding='utf-8') as inwo:
    for line in inwo:
        print(line)

with open('shakespeare.txt', 'w') as fopen:
    message = 'Be or Not To Be'
    print(message) # wyswietli na standardowe wyjście
    print(message, file = fopen) # zapis do pliku
    # Można ustawić zarówno parametr file i wyświetlić wartość na ekrani
    # potrzebujemy przekazać wartość None, bezpośrednio lub za pomocą zmiennej
    nofile = None
    print(message, file = nofile) # wyswietli na standardowe wyjście
    print(message, file = None)