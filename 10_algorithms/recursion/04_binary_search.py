# Write a function for binary search, which take 2 parameters - wanted element and list of elements.
# It returns info, is wanted element is on the list or not.
# Input:
# data = [3, 15, 45, 2, 6, 12, 44, 34, 21, 56, 7, 3, 12]
# elem = 21
# Output:
#     “Number 21 is on the list”
data = [3, 15, 45, 2, 6, 12, 44, 34, 21, 56, 7, 3, 12]
elem = 22
data.sort()


def binary_search(n, d):
    si = 0
    ei = len(d)
    mi = (si + ei) // 2
    if n == d[mi]:
        print(f'Number {n} is on the list.')
    elif n < d[mi]:
        ei = mi - 1
        binary_search(n, d[si:ei])
    elif n > d[mi]:
        si = mi + 1
        binary_search(n, d[si:ei])
    else:
        print(f'Number {n} is not on the list.')


binary_search(elem, data)



