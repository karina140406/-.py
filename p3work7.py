a = [1, 2, 4, 3]
mid = len(a) // 2
sum_left = sum(a[:mid])
sum_right = sum(a[mid:])
result = sum_left == sum_right
print(sum_left)
print(sum_right)
print(result)