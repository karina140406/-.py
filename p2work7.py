import random
list = [1,2,3,4,5,5,4,3,2,1,5]
index_2 = list.index(2)
list.insert(index_2 + 1, 'a')
numbers = []
for _ in range(10):
    numbers.append(random.randint(10,100))
combined = list + numbers
count_5 = combined.count(5)
print(combined)
print(count_5)