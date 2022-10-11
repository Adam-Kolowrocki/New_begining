# Write a function which calculate circle field from given radius.
def circ_field(r):
    """This function returns field of circle of given radius."""
    field = 3.14 * (r * r)
    return field


r = int(input(f'Type radius of circle to calculate field ->'))
print(f'The field of circle with given radius {r} is = {circ_field(r)}.')
