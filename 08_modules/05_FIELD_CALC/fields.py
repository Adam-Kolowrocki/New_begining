import fields_modules

shapes = 'You can chose from the following shapes: \n1 - triangle \n2 - square \n3 - rectangle \n4 - diamond ' \
         '\n5 - trapeze \n6 - hexagon \n7 - octagon'


def main():
    """This script calculate field of a building/flat from user data"""
    total_field_calc(menu())


def menu():
    """Menu of the script"""
    print(f'You can calculate field of flat/building by specifying number of rooms, their shape and dimensions.')
    rooms_number = int(input(f'How many rooms You want to add -> '))
    return rooms_number


def user_shape(room_number):
    """Collect room shape from user"""
    print(shapes)
    options = ['1', '2', '3', '4', '5', '6', '7']
    chosen_shape = '0'
    while chosen_shape not in options:
        chosen_shape = input(f'What is the shape of room no. {room_number} -> ')
    return chosen_shape


def get_dimensions(shape):
    """Collect dimensions from user"""
    if shape == '2' or shape == '6' or shape == '7':
        a = int(input(f'Type the length of one wall in meters -> '))
        return a
    elif shape == '1' or shape == '4':
        a = int(input(f'Type the length of one wall in meters -> '))
        h = int(input(f'Type the distance from one corner of the room to the perpendicular wall in meters -> '))
        return a, h
    elif shape == '3':
        a = int(input(f'Type the length of first wall of rectangular shape room in meters -> '))
        b = int(input(f'Type the length of second wall of rectangular shape room in meters -> '))
        return a, b
    else:
        a = int(input(f'Type the length of first (base) wall of trapeze shape room in meters -> '))
        b = int(input(f'Type the length of second (base) wall of trapeze shape room in meters -> '))
        h = int(input(f'Type the shortest distance from one to another base wall of trapeze shape room in meters -> '))
        return a, b, h


def room_field(shape):
    """Calculate fields of rooms with shape and dimensions from user."""
    if shape == '1':
        a, h = get_dimensions(shape)
        return fields_modules.triangle(a, h)
    elif shape == '2':
        a = get_dimensions(shape)
        return fields_modules.square(a)
    elif shape == '3':
        a, b = get_dimensions(shape)
        return fields_modules.rectangle(a, b)
    elif shape == '4':
        a, h = get_dimensions(shape)
        return fields_modules.diamond(a, h)
    elif shape == '5':
        a, b, h = get_dimensions(shape)
        return fields_modules.trapeze(a, b, h)
    elif shape == '6':
        a = get_dimensions(shape)
        return fields_modules.hexagon(a)
    elif shape == '7':
        a = get_dimensions(shape)
        return fields_modules.octagon(a)


def total_field_calc(rooms):
    total_field = 0
    room_number = 1
    while rooms > 0:
        total_field += room_field(user_shape(room_number))
        rooms -= 1
        room_number += 1
    print(f'\n\nTotal field of the flat/house is {total_field}m2')


if __name__ == "__main__":
    main()
