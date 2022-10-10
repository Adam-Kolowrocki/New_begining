# Create dictionary for 10 European countries which contain lists of 10 the most popular female names.
# Sum all lists. New list should contain 100 elements.
# Print only that names, which appears in at least 3 countries.
eu_countries = {'Poland': ['Ana', 'Carolina', 'Hana', 'Victoria', 'Barbra', 'Sophia', 'Margareth', 'Monic', 'Katarina',
                           'Eva'],
                'Germany': ['Emilia', 'Hanna', 'Mia', 'Emma', 'Sophia', 'Mila', 'Lina', 'Ella', 'Leah', 'Marie'],
                'France': ['Jade', 'Louisa', 'Emma', 'Alice', 'Amber', 'Lina', 'Pink', 'Chloe', 'Mia', 'Leah'],
                'Spain': ['Lucy', 'Sophia', 'Martha', 'Mary', 'Julia', 'Paula', 'Emma', 'Danielle', 'Valerie', 'Dawn'],
                'Italy': ['Anna', 'Giuseppina', 'Rose', 'Angela', 'Giovanna', 'Sofia', 'Giulia', 'Aurora', 'Alice',
                          'Geneva'],
                'Chech Republic': ['Teresa', 'Veronica', 'Michaela', 'Anna', 'Adela', 'Clare', 'Jana', 'Martin',
                                   'Peter', 'Elisabeth'],
                'Slovakia': ['Maria', 'Anna', 'Zuzana', 'Katarina', 'Eve', 'Jana', 'Helena', 'Monika', 'Marta',
                             'Martina'],
                'UK': ['Olivia', 'Amelia', 'Isla', 'Ava', 'Ivy', 'Freya', 'Lily', 'Florence', 'Mia', 'Willow'],
                'Sweden': ['Alice', 'Olivia', 'Astrid', 'Maya', 'Vera', 'Ebb', 'Ella', 'Wilma', 'Alma', 'Lily'],
                'Norway': ['Kari', 'Marit', 'Ingrid', 'Life', 'Maria', 'Ida', 'Eve', 'Anna', 'Sophia', 'Lea']
                }
sum_list = []
for key in eu_countries:
    sum_list += eu_countries[key]
popular_names = []
for name in sum_list:
    if sum_list.count(name) >= 3:
        popular_names.append(name)
popular_names = set(popular_names)
print(f'The most popular female names in Europe are : ')
for name in popular_names:
    print('                                              ', name)
