#  In the poem count the occurrence of each word, ignore letter size.
# """Szybko, zbudź się, szybko, wstawaj
# Szybko, szybko, stygnie kawa
# Szybko, zęby myj i ręce"""
#
# Print it in a nice way, eg.:
#     szybko : 5
#     zbudź : 1
poem = """Szybko, zbudź się, szybko, wstawaj
Szybko, szybko, stygnie kawa
Szybko, zęby myj i ręce"""
poem.lower()
words_list = poem.split(' ')
print(words_list)
words = {}
for word in words_list:
    if word not in words:
        words[word] = 1
    elif word in words:
        words[word] += 1
print(words)
