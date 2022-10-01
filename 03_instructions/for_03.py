# Write a code, which will return sum of predecessors for 10 consecutive natural numbers.
# Expected result: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55
sum_pre = 0
sum_list = []
for i in range(1, 11):
    sum_pre += i
    sum_list.append(sum_pre)
print(sum_list)
