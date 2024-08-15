def get_matrix(n, m, value):
    matrix = []
    for i in range(0,n):
        matrix.append([])
        for j in range(0,m):
            matrix[i].append(value)
    return matrix

print(get_matrix(1,2,3))
print(get_matrix(10,20,30))
print(get_matrix(100,2,3))