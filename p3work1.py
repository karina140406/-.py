numbers_list = [1, 5, 3, 3, 5]
numbers_list_ordered = sorted(numbers_list, reverse=True)
numbers_set = set(numbers_list) | {max(numbers_list) + 1} 
numbers_frozenset = frozenset(set(numbers_list) - {min(numbers_list)}) 
print(numbers_list)
print(numbers_list_ordered)
print(numbers_set)
print(numbers_frozenset)