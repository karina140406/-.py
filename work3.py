n = int(input('Введите колличество секунд'))
hours = n // 3600
ramaining_seconds = n % 3600
minuts = ramaining_seconds // 60
seconds = ramaining_seconds % 60
print(f'Результат - {hours} часов, {minuts} минут, {seconds} секунд')