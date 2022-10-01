# Create a list of ingredients for Your favorite dish.
# Print, what You should add in order.
# Outside the loop add additional instructions, eg. “Into the oven”, “Serve cooled”.
ingredients = ['eggs withes', 'sugar', 'eggs yolks', 'flour', 'vanilla', 'milk', 'condensed milk', 'tofi']
for i in ingredients:
    print(i)
    if i == 'eggs withes':
        print('whip to a stiff foam...')
    elif i == 'sugar':
        print('Add in smal portions...')
    elif i == 'eggs yolks':
        print('add one at a time while still whisking')
    elif i == 'flour':
        print('Add in small portions, stirring gently with a spatula and add last ingredient')
    elif i == 'vanilla':
        print('Pour the dough into a tighter bowl and bake it in an oven preheated to 170 degrees for about 30 minutes')
        print('Let the dough cool, cut into portions and prick with a toothpick')
    elif i == 'milk':
        print('Mix with')
    elif i == 'condensed milk':
        print('Pour the dough')
        print('At the end put the')
    elif i == 'tofi':
        print('on the top of the cake...')
print('Enjoy')

