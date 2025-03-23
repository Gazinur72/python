def max_number(a, b):
    if a > b:
        return a
    else:
        return b


def empty_function():
    pass


def even_numbers(n):
    for number in range(0, n + 1):
        if number % 2 == 0:
            yield number


def test_max_number():
    assert max_number(10, 5) == 10
    assert max_number(3, 7) == 7
    assert max_number(-5, -10) == -5
    assert max_number(0, 0) == 0

for num in even_numbers(10):
    print(num)

test_max_number()
print("Все тесты пройдены!")

