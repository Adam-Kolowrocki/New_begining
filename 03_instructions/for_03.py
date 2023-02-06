# Write a code, which will return sum of predecessors for 10 consecutive natural numbers.
# Expected result: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55
sum_pre = 0
for i in range(1, 10):
    sum_pre += i
    print(sum_pre, end=', ')
print(sum_pre + 10)
