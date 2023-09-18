import math
print('Выберите действие: ')
print('1. Сложить два числа')
print('2. Вычесть первое из второго')
print('3. Перемножить два числа')
print('4. Разделить первое на второе')
print('5. Возвести в степень N первое число')
print('6. Найти квадратный корень из первого числа')
print('7. Найти факториал числа')
print('8. Найти синус первого числа')
print('9. Найти косинус первого числа')
print('10. Найти тангенс первого числа')
action = input()
while True:
    try:
        if action == '1':
            num1 = float(input('Введите первое число: '))
            num2 = float(input('Введите второе число: '))
            result = num1 + num2
            result = str(result)
            print('Результат ' + result)
        elif action == '2':
            num1 = float(input('Введите первое число: '))
            num2 = float(input('Введите второе число: '))
            result = num1 - num2
            result = str(result)
            print('Результат ' + result)
        elif action == '3':
            num1 = float(input('Введите первое число: '))
            num2 = float(input('Введите второе число: '))
            result = num1 * num2
            result = str(result)
            print('Результат ' + result)
        elif action == '4':
            num1 = float(input('Введите первое число: '))
            num2 = float(input('Введите второе число: '))
            if num2 == 0:
                print('На ноль делить нельзя!')
            else:
                result = num1 / num2
                result = str(result)
                print('Результат ' + result)
        elif action == '5':
            num1 = float(input('Введите число: '))
            num2 = float(input('Введите степень, в которое нужно возвести число: '))
            result = num1 ** num2
            result = str(result)
            print('Результат ' + result)
        elif action == '6':
            num1 = float(input('Введите первое число: '))
            result = math.sqrt(num1)
            result = str(result)
            print('Результат ' + result)
        elif action == '7':
            num1 = int(input('Введите число: '))
            result = math.factorial(num1)
            result = str(result)
            print('Результат ' + result)
        elif action == '8':
            num1 = float(input('Введите  число: '))
            result = math.sin(num1)
            result = str(result)
            print('Результат ' + result)
        elif action == '9':
            num1 = float(input('Введите первое число: '))
            result = math.cos(num1)
            result = str(result)
            print('Результат ' + result)
        elif action == '10':
            num1 = float(input('Введите первое число: '))
            result = math.tan(num1)
            result = str(result)
            print('Результат ' + result)
        break
    except ValueError:
        print("Ой че то не то, попробуй снова:)")