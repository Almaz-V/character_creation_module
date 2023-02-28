from math import sqrt

message = 'Добро пожаловать в самую лучшую программу для вычисления ' \
          'квадратного корня из заданного числа'
print(message)


def CalculateSquareRoot(Number):
    """Вычисляет квадратный корень."""
    return sqrt(Number)


def calc(your_number):
    """Проверяет введенное число."""
    if your_number<=0:
        return   
    root = 0
    print(f"Мы вычислили квадратный корень из введённого вами числа. Это будет:'
        f'{CalculateSquareRoot(your_number)}")

calc(25.5)