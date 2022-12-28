# Stwórz moduł, który zajmuje się jedynie otwieraniem plików
# - oferuje bezpieczny sposób odczytu oraz bezpieczny zapis.
# Funkcja czytająca pliki sprawdza najpierw czy dany plik istnieje oraz czy jest niepusty.
# Funkcja zapisująca do pliku chroni przed nadpisaniem istniejącego pliku.
import os


def main():
    file_reader(user_data('read'))
    file_writer(user_data('written'), data_to_save())


def user_data(action):
    filename = input(f'Type the name of file to be {action}, with extension -> ')
    return filename


def data_to_save():
    to_save = input(f'Type, what do You want to save -> ')
    return to_save


def file_reader(filename):
    if os.path.exists(f'./{filename}'):
        if os.path.getsize(f'./{filename}'):
            with open(f'./{filename}', 'r') as file:
                data = file.read()
            print(f'Treść odczytana z pliku = {data}')
            return data
    else:
        print(f'No such file -> {filename}')


def file_writer(filename, data):
    with open(f'./{filename}', 'a+') as file:
        file.write(f'\n{data}')


if __name__ == "__main__":
    main()
