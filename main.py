print("Сложение")
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
result1 = num1 + num2
print("Результат сложения:", result1)

print("Вычитание")
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
result1 = num1 - num2
print("Результат:", result1)

print("Умножение")
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
result1 = num1 * num2
print("Результат:", result1)

print("Деление")
try:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    result = num1 / num2

except ValueError:
    print("Ошибка: введено не число!")
except ZeroDivisionError:
    print("Ошибка: Деление на ноль!")
else:
    print(f"Результат: {result}")
finally:
    print("Программа завершина.")
