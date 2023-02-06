# Create a tuple which contains Your PET details (Type, race, name).
# Unpack Tuple into single variables. Use variables to print f-string,
# to create sentence like this: "My dog, race of border collie has a name Dante".
pet_tuple = ('dog', 'Shitsu', 'Roger')
(type, race, name) = pet_tuple
print(f'My {type}, of race {race} has a name {name}.')
