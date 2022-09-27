quote = "Honesty is the first chapter in the book of wisdom."
# count characters in quota
print('String contains', quote.count(''))
print('But the length of string is', len(quote))
# Print "wisdom" with no modifications of quota string
print(quote[-7:-1])
# Print only first half of quota
print('First half = ', quote[:len(quote) // 2])
# Print only a dot
print(quote[-1])
# Print from middle every 3 letter
print(quote[len(quote) // 2::3])
# Print "Hnsyi h is hpe ntebo fwso."
print(quote[::2])
# Print all backwards
print(quote[::-1])
# Replace "wisdom" with "friendship"
print(quote.replace('wisdom', 'friendship'))
