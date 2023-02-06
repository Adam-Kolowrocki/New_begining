# Create a listo of items, which You will take for a trip to mountains.
# Sort items alphabetically and print.
item_list = ['backpack', 'chocolate', 'jacket', 'water', 'sleeping bag', 'tent', 'phone', 'buts', 'torch', 'hot beverage']
print(f'List before sorting -> {item_list}')
print(f'Items list sorted with "sorted" -> {sorted(item_list)}')
print(f'Original list ("sorted" do not change original object) -> {item_list}')
item_list.sort()
print(f'Items list sorted with "sort -> " {item_list}')
