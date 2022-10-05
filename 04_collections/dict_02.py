# Create tuple tuples_to_dict containing 2 elements tuples.
# Convert it into dictionary dict_from_tuples.
tuples_to_dict = (
    ('jabłko', 'apple'),
    ('gruszka', 'pear'),
    ('śliwka', 'plum'),
    ('wiśnia', 'chery'),
    ('truskawka', 'strawberry')
)
dict_from_tuples = dict(tuples_to_dict)
print(dict_from_tuples)
print(dict_from_tuples['gruszka'])
