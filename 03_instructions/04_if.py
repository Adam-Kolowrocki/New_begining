# Create variable holding the string.
# Check if the string is longer than 5 and those it contains "a".
# If it those, replace all "a" with "z" and print the string.
var_str = 'abrakadabra'
if len(var_str) > 5 and "a" in var_str:
    print(var_str.replace("a", "z"))
else:
    print('Conditions not net.')

