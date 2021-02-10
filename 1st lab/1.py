yourChoice = int(input("Какой вариант вы хотите выбрать (1 / 2 / 3 / 4): "))

def options(yourChoice):
    a = int(input("Введите A: "))
    b = int(input("Введите B: "))
    c = int(input("Введите C: "))
    if yourChoice == 1:
        k = int(input("Введите K: "))
        if (a == 0) or (b == 0) or (a + b + c * (k - a / b**3) == 0):
            return "Error: Деление на ноль"
        return abs(((a**2 / b**2) + (c**2 * a**2)) / (a + b + c * (k - a / b**3)) + c + (k/b - k/a)*c)
    if yourChoice == 2:
        d = int(input("Введите D: "))
        k = int(input("Введите K: "))
        if (a == 0) or (b == 0):
            return "Error: Деление на ноль"
        return abs(((a**2 - b**3 - c**3 * a**2) * (b - c + c * (k - d / b**3)) - (k / b - k / a) * c)**3 - 20000)
    if yourChoice == 3:
        if (c - a == 0):
            return "Error: Деление на ноль"
        return abs(1 - a * b**c - a * (b**2 - c**2) + (b - c + a) * (12 + b) / (c - a))
    if yourChoice == 4:
        d = int(input("Введите D: "))
        f = int(input("Введите F: "))
        if (a == 0):
            return "Error: Деление на ноль"
        return abs(a - b * c * d**3 + (c**5 - a**2)/a + f**3 * (a - 213))

print(options(yourChoice))
