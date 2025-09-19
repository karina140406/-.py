sleep = int(input('Введите продолжительность сна в минутах'))
m = sleep / 60
if (m>=7 and m<=9):
 optimal_sleep_duration = True
else:
 optimal_sleep_duration = False
print(f'Оптимальная продолжительность сна: {optimal_sleep_duration}')