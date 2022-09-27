# Ask user about title, autor name and pages of a book
title = input('Type a title of a book: ')
name = input('Type a name of the author: ')
pages_num = input('And a number of pages: ')
print(title.isalpha())
print(name.isalpha())
print(pages_num.isnumeric())
