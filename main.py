print("Калькулятор")
num1 = float(input("Введите первое число:"))
num2 = float(input("Введите второе число:"))

message = '''
Выберите математическую операцию:

+ сложение
- вычитание
/ деление
* умножение
'''

operation = input(message)

if operation == '+':
    print('Сложение')
    result = num1 + num2
elif operation == '-':
    print('Вычитание')
    result = num1 - num2
elif operation == '/':
    print('Деление')
    result = num1 / num2
elif operation == '*':
    print('Умножение')
    result = num1 * num2
else:
    print('Неизвестная операция')

print("Результат:", result)

