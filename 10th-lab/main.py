from time import sleep


matrix = [
    [1, 2, 3, 4, 5, 6, 7, 8],
    [8, 7, 6, 5, 4, 3, 2, 1],
    [2, 3, 4, 5, 6, 7, 8, 9],
    [9, 8, 7, 6, 5, 4, 3, 2],
    [1, 3, 5, 7, 9, 7, 5, 3],
    [3, 1, 5, 3, 2, 6, 5, 7],
    [1, 7, 5, 9, 7, 3, 1, 5],
    [2, 6, 3, 5, 1, 7, 3, 2],
]

def close_program(key):
    if key == '' or key == 'N':
        print('Выход из программы...')
        for _ in range(2):
            sleep(0.5)
            print('...')
        exit()

def multiplication():
    multiplicationAll = 1
    for row in matrix:
        multiplication = 1
        for item in row:
            multiplication *= item; multiplicationAll *= item
        print(f'Умножение элементов строки: {multiplication}')
    return f'Умножение элементов всех строк: {multiplicationAll}'

def sumElements():
    sum = 0
    for row in matrix:
        for item in row:
            sum += item
    return sum

def elementsSum():
    sumL = 0; sumH = 0
    for row in matrix:
        for item in row:
            if item < 5:
                sumL += item
            else:
                sumH += item
    if sumL > sumH:
        return f'Сумма чисел < 5: {sumL}'
    else:
        return f'Сумма чисел >= 5: {sumH}'

def Zero():
    cot = 0
    for row in matrix:
        for count in range(len(row)):
            row[count] = 0
        matrix[cot] = row
        cot += 1
    return matrix

def call(key):
    allFunc = {
        '1': multiplication, '3': elementsSum,
        '2': sumElements, '4': Zero
    }
    return allFunc.get(key)()

while True:
    print('\nСписок всех возможностей:\n\t1 - умножение по строкам\n\t2 - сложение всех элементов матрицы\n\t3 - сложения всех элементов матрицы меньших 5 и всех элементов матрицы больше или равных\n\t4 - замена значений всех элементов матрицы на 0')
    key = input('\nВаш выбор:\n\t> ')
    close_program(key)
    print(call(key))
    key = input('Вы хотите продолжить? [Y]-Yes [N]-No\n\t> ')
    close_program(key)
