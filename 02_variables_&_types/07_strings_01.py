# Create odd variable longer than 7
# Return string of 3 middle characters
test_string = 'Mammamijamayamniema'
middle = len(test_string) // 2
middle_string = test_string[middle - 1:middle + 2]
print('String of 3 middle characters of test string is ->', middle_string)
