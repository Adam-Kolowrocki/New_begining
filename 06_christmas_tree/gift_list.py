# What for a gift?
# Create list of gifts ideas for your loved ones.
# When time came (holiday, birthday, anniversary), program randomly choose a gift and maybe a place to give it.

from random import choice
gifts = ['spa voucher', 'weekend with family', 'weekend for Your self', 'watch', '2h of play', 'good wine', 'flowers']
places = ['restaurant', 'home', 'park', 'bedroom', 'anywhere']


def choose_gift(occasion):
    gift = choice(gifts)
    place = choice(places)
    if occasion == 'a':
        occ = 'anniversary'
    elif occasion == 'b':
        occ = 'birthday'
    else:
        occ = 'holiday'
    print(f'For {occ} the best gift I thin is a "{gift}" and You should give it in {place}.')


def main():
    print(f'This program will help You to give a right gift in a right place for Your loved ones...')
    print(f'\nIt can help with holidays "h", birthday "b" and anniversary "a".')
    options = ['a', 'b', 'c']
    occasion = input(f'What is the occasion ->')
    while occasion not in options:
        print(f'You have chosen unknown occasion...')
        occasion = input(f'What is the occasion ->')
        continue
    choose_gift(occasion)


main()

