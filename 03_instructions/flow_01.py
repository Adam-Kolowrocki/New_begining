# Let the User to input any number of names in one string (eg. divided with coma or space).
# Say "Hello" to everyone in the list.
names = input(f'Insert a list of names separated with "," -> ')
names_list = names.split(",")
for name in names_list:
    print(f' Hello {name}, how are You?')
