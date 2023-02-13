# Write a function for binary search, which take 2 parameters - wanted element and list of elements.
# It returns info, is wanted element is on the list or not.
# Input:
# data = [3, 15, 45, 2, 6, 12, 44, 34, 21, 56, 7, 3, 12]
# elem = 21
# Output:
#     “Number 21 is on the list”
data = [3, 15, 45, 2, 6, 12, 44, 34, 21, 56, 7, 3, 12]
elem = 21
data.sort()
low_i = 0
hi_i = len(data) - 1


def binary_search_iter(x, lis, low, hi):
    while low <= hi:
        mi = (low + hi) // 2
        if low == hi and lis[low] != x:
            return f"Number {x} is not in the list"
        elif x == lis[mi]:
            return f"Number {x} is in the list"
        elif x < lis[mi]:
            hi = mi - 1
            continue
        elif x > lis[mi]:
            low = mi + 1
            continue


def binary_search_rec(x, lis, low, hi):
    if low > hi:
        return f"Number {x} is not in the list"
    mi = (low + hi) // 2
    if x == lis[mi]:
        return f"Number {x} is in the list"
    elif x < lis[mi]:
        hi = mi - 1
        return binary_search_iter(x, lis, low, hi)
    elif x > lis[mi]:
        low = mi + 1
        return binary_search_iter(x, lis, low, hi)


print(binary_search_iter(elem, data, low_i, hi_i))
print(binary_search_rec(elem, data, low_i, hi_i))
