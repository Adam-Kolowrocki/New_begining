# Take a 3 opinions about a book.
# Calculate medium opinion. Depending of the result, print info.
# If the opinion is grater then 7 - Very good, opinion 5-7 average,
# 4 and less - not worth attention.
print('For future readers, give Your opinion about the book...')
print('Use numbers from 1 to 10.')
opinion_1 = int(input('How do You rate the story ->'))
opinion_2 = int(input("How do You rate the writer's style ->"))
opinion_3 = int(input('How do You rate the cover graphics ->'))
medium = (opinion_1 + opinion_2 + opinion_3) / 3
if medium >= 7:
    print('The book is very good.')
elif 7 > medium >= 5:
    print('The book is average.')
else:
    print('The book is not worth of Your attention.')
