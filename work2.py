from math import*
a = int(input('Введите сторону a-'))
b = int(input('Введите сторону b-'))
c = int(input('Введите сторону c-'))
p = (a + b + c) / 2
area = sqrt(p * (p-a) * (p-b) * (p-c))
print(f'Периметр {p} Площадь {area}')