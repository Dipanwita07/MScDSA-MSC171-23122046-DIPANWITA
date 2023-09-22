
rows_1 = int(input("Enter the number of rows for matrix 1: "))
cols_1 = int(input("Enter the number of columns for matrix 1: "))

# Initialize an empty matrix 1
A = []
print("Enter elements for matrix A:")
for i in range(rows_1):
    row = []
    for j in range(cols_1):
        element = float(input(f"Enter element at position ({i+1},{j+1}): "))
        row.append(element)
    A.append(row)


rows_2 = int(input("Enter the number of rows for matrix 2: "))
cols_2 = int(input("Enter the number of columns for matrix 2: "))


B = []
print("Enter elements for matrix 2:")
for i in range(rows_2):
    row = []
    for j in range(cols_2):
        element = float(input(f"Enter element at position ({i+1},{j+1}): "))
        row.append(element)
    B.append(row)
if cols_1 != rows_2:
    print("Matrix multiplication is not possible. The number of columns in matrix A must be equal to the number of rows in matrix B.")
else:
    # Continue with matrix multiplication
# Initialize a result matrix with zeros
  result = [[0 for __for in range(cols_2)] for _ in range(rows_1)]

# Perform matrix multiplication
for i in range(rows_1):
    for j in range(cols_2):
        for k in range(cols_2):
            result[i][j] += A[i][k] * B[k][j]

# Print the result matrix
print("Result of matrix multiplication:")
for row in result:
    print(row)
# Take user input for the dimensions and elements of matrices A and B (as shown above).

# Check if matrices can be multiplied.

if cols_1 != rows_2:
    print("Matrix multiplication is not possible. The number of columns in matrix A must be equal to the number of rows in matrix B.")
else:
    # Initialize a result matrix with zeros
    result = [[0 for _ in range(cols_2)] for _ in range(rows_1)]

    # Perform matrix multiplication
    for i in range(rows_1):
        for j in range(cols_2):
            for k in range(cols_1):
                result[i][j] += A[i][k] * B[k][j]

    # Print the result matrix
    print("Result of matrix multiplication:")
for row in result:
    print(row)