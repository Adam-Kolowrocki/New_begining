# write a function checking if elements of first tuple ar in second tuple
tuple_1 = (3, 4, 5)
tuple_2 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)


def tuple_in_tuple():
    for i in tuple_1:
        if i not in tuple_2:
            return False
    return True


print(tuple_in_tuple())


