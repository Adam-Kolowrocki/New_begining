# Compare discard() vs remove() for a type set.
test_set = {3, 5, 7, 8, 9, 0, 1, 2, 4, 6}
print(test_set)
test_set.discard(6)
print(test_set)
test_set.remove(9)
print(test_set)
test_set.discard(6)
test_set.remove(9)
