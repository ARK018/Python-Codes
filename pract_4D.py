
def matrix_multiplication(matrix1, matrix2):
    rows1, cols1 = len(matrix1), len(matrix1[0])
    rows2, cols2 = len(matrix2), len(matrix2[0])

    if cols1 != rows2:
        print("Matrix multiplication is not possible.")
        exit()

    result = [[0 for _ in range(cols2)] for _ in range(rows1)]
    
    for i in range(rows2):
        for j in range(cols2):
            for k in range(rows1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result

def get_matrix_elements(rows, cols):
    matrix = [] 
    for i in range(rows):
        rows = []
        for j in range(cols):
            value = int(input(f"Enter element at position {i+1},{j+1} : "))
            rows.append(value)
        matrix.append(rows)
    return matrix   

def print_matrix(matrix):
    for row in matrix:
        print(row)


rows1 = int(input("Enter no. of rows in Matrix 1 : "))
cols1 = int(input("Enter no. of rows in Matrix 1 : "))
matrix1 = get_matrix_elements(rows1, cols1)

rows2 = int(input("\nEnter no. of rows in Matrix 2 : "))
cols2 = int(input("Enter no. of columns in Matrix 2 : "))
matrix2 = get_matrix_elements(rows2, cols2)

result = matrix_multiplication(matrix1, matrix2)

print("\nMatrix1")
print_matrix(matrix1)

print("\nMatrix2")
print_matrix(matrix2)

print("\nMultiplication of Matrix1 and Matrix2")
print_matrix(result)