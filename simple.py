n = int(input('Введите число: '))
max = 0
for n in range(1, n):
    n = n + 1
    if (n > max) and (n % 5 == 0):
        max = n
print(max)