# Initialize the dictionary to store matrices
matrix = {
    "matrix 1": [],
    "matrix 2": [],
    "result matrix": []
}
matrix = []
while True:
        
            rows = int(input(f"Enter the number of rows for {matrix}: "))
            cols = int(input(f"Enter the number of columns for {matrix}: "))
            if rows <= 0 or cols <= 0:
                print("Rows and columns must be positive integers.")
                
            break

print(f"Enter elements for {matrix} row-wise:")
for i in range(rows):
        while True:
        
                row = [float(x) for x in input(f"Enter values for row {i + 1}: ").split()]
                if len(row) != cols:
                    print(f"Row must have {cols} elements.")
                    continue
                break
                matrix.append(row)

matrix_dict[matrix_key] = matrix

def process_matrices():
    """Calculates the result matrix and stores it in the dictionary."""

    if not matrix_dict["matrix 1"] or not matrix_dict["matrix 2"]:
        print("Both matrix 1 and matrix 2 must be entered first.")
        return

    matrix1 = matrix_dict["matrix 1"]
    matrix2 = matrix_dict["matrix 2"]

    result_matrix = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            element = 0
            for k in range(len(matrix1[0])):
                element += matrix1[i][k] * matrix2[k][j]
            row.append(element)
        result_matrix.append(row)

    matrix_dict["result matrix"] = result_matrix

def display_result_to_file(filename):
    """Displays the result matrix to a file.

    Args:
        filename: The filename to save the result to.
    """

    result_matrix = matrix["result matrix"]
    with open(filename, "w") as file:
        for row in result_matrix:
            file.write(" ".join(map(str, row)) + "\n")
    print(f"Result matrix has been saved to '{filename}'.")

def menu():
    """Displays a menu to the user and allows them to enter matrices, calculate the result matrix, and display the result matrix to a file."""

    while True:
        print("\nMatrix Multiplication Menu:")
        print("1. Enter Matrix 1")
        print("2. Enter Matrix 2")
        print("3. Calculate")
        print("4. Export Result to File")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            matrix("matrix 1")
        elif choice == "2":
            matrix("matrix 2")
        elif choice == "3":
            process_matrices()
        elif choice == "4":
            if not matrix["result matrix"]:
                print("Matrix multiplication result is not available.")
            else:
                filename = input("Enter the filename to save the result to: ")
                display_result_to_file(filename)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please choose a valid option.")

    menu()
