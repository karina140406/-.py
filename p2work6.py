import random
numbers = []
for _ in range(10):
    numbers.append(random.randint(10,100))
total = sum(numbers)
average = total / len(numbers)
print("Список:" , numbers)
print("Сумма элементов:", total)
print("Среденее значение:", average)