print("Введите матрицу построчно (каждый элемент матрицы через пробел)"); i = 1; matrix = []; sum = 0
while True:
    print(f"{i}-ая строка матрицы: ", end="")
    some_matrix = list(map(int, input().split()))
    if some_matrix == []:
        break
    for _ in some_matrix:
        sum += _
    matrix.append(some_matrix)
    i += 1

print(f"Ответы:\nМатрица: {matrix}\nСумма всех элементов матрицы: {sum}")
