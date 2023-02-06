# Take from User random text, print only even signs.
# Use two ways, loop and sting slicing to return ( ‘abrakadabra’ -> ‘baaar’).

user_text = input('Give a random text to process -> ')

# using string slicing method
# user_text = 'abrakadabra'
print(f'User text is "{user_text}".')
print(f'Even letters from user text with string slicing is "{user_text[1::2]}".')

# using loop method
new_text = ''
for i in range(1, len(user_text)):
    if i % 2 == 1:
        new_text += user_text[i]
print(f'Even letters from user text with loop method is "{new_text}".')
