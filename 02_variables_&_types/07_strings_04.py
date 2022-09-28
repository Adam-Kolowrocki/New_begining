# Ask user about title, autor name and pages of a book
title = input('Type a title of a book: ')
name = input('Type a name of the author: ')
pages_num = input('And a number of pages: ')
print('Is title alphabetic = ', title.replace(" ", "").isalpha())
print('Is author name alphabetic = ', name.replace(" ", "").isalpha())
print('Is numer of pages numeric = ', pages_num.isnumeric())
title = title.title()
name = name.title()
print('Corrected title is = ', title)
print('Corrected author name is = ', name)
book = title + " " + name + " " + pages_num
print('String "book" is', len(book), 'characters long.')
