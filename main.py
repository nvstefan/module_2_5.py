# Домашняя работа по уроку:
# "Функции в Python.Функция с параметром"

def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        i = []
        for j in range(m):
            i.append(value)
        matrix.append(i)
    return matrix
result1 = get_matrix(3, 3, 11)
result2 = get_matrix(4, 5, 3)
result3 = get_matrix(2, 3, 55)
print(result1)
print(result2)
print(result3)

