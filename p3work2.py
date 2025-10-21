list_1 = [3, 4, 1, 2, 5]
list_2 = [6, 8, 7, 9]
list_2.sort()
list_1.sort(reverse=True)
list_3 = sorted(list_1 + list_2)
list_3_len = len(list_3)
print(list_1)
print(list_2)
print(list_3)
print(list_3_len)