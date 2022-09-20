while True:
    try:
        a = int(input('Введите первое число: '))
        b = int(input('Введите второе число: '))
        y = int(input("Введите номер операции: \n1 - Сложение\n2 - Вычитание\n3 - Умножение\n4 - Деление\n"))
    except:
        print('Введенный элемент не является числом, введите число!')
        continue
    break

if y == 1:
    print(a + b)
elif y == 2:
    print(a - b)
elif y == 3:
    print(a * b)
elif y == 4:
    print(a / b)
else:
    print('Вы решили начать какую-то странную операцию')
