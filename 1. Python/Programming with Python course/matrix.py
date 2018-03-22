# The matrix program
# Written by japoveda10

# Print title function
def print_title():
    print("-------------------------------------------------------------")
    print("-               Welcome to the matrix program               -")
    print("-------------------------------------------------------------")

# Print instructions function
def print_instructions():
    print("(1) Instructions \n")
    print("With this program, you can create a matrix, put values inside it, apply a ")
    print("square or multiply by a number function to all elements of the matrix, ")
    print("transpose the matrix or print it.")

# Apply square function
def applySquare(matrix, num_rows, num_columns):

    # For each element inside the matrix, multiply it by itself
    for i in range(num_rows):
        for j in range(num_columns):
            matrix[i][j] = matrix[i][j] * matrix[i][j]

    # Prints informative message
    print("This is your matrix after applying square: \n")

    # Prints matrix
    printMatrix(matrix, num_rows, num_columns)

# Apply multiply function
def applyMultiply(matrix, num_rows, num_columns, multiply_number):

    # For each element inside the matrix, multiply it by multiply_number
    for i in range(num_rows):
        for j in range(num_columns):
            matrix[i][j] = matrix[i][j] * multiply_number

    # Prints informative message
    print("This is your matrix after applying multiply: \n")

    # Prints matrix
    printMatrix(matrix, num_rows, num_columns)

# Transpose function
def transpose(matrix, num_rows, num_columns):

    # List that will store original matrix values
    listOfOriginalMatrixValues = []

    # Adds elements to listOfOriginalMatrixValues
    for i in range(num_rows):
        for j in range(num_columns):
            listOfOriginalMatrixValues.append(matrix[i][j])

    # Creates new matrix
    transposedMatrix = []

    # Adds 0´s to transposed matrix
    for i in range(num_columns):
        transposedMatrix.append([])

        for j in range(num_rows):
            transposedMatrix[i].append(0)

    # Number used to get elements from listOfOriginalMatrixValues
    number = 0;

    # Adds elements to new transposed matrix
    for i in range(num_rows):
        for j in range(num_columns):
            transposedMatrix[j][i] = listOfOriginalMatrixValues[number]
            number = number + 1

    # Prints informative message
    print("This is your transposed matrix: \n")

    # Prints matrix
    printMatrix(transposedMatrix, num_columns, num_rows)

    # Return transposed matrix
    return transposedMatrix

# Print matrix function
def printMatrix(matrix, num_rows, num_columns):

    for i in range(num_rows):
        row = ""
        for j in range(num_columns):
            row += "%d\t" % (matrix[i][j])
        print(row)

# Print ending message function
def printEndingMessage():
    print("-------------------------------------------------------------")
    print("-           Thank you for using the matrix program          -")
    print("-------------------------------------------------------------")

# Main function
def main():
    # Prints the title
    print_title()

    # Prints a space
    print("")

    # Prints the welcome message
    print("Hello! Welcome to the matrix program! \n")

    # Prints instructions
    print_instructions()

    # Prints a space
    print("")

    # Prints instructions
    print("(2) Please enter the matrix dimensions: \n")

    # Number of rows entered by the user
    num_rows = int(input("(2.1) Enter number of rows: "))

    # Number of columns entered by the user
    num_columns = int(input("(2.2) Enter number of columns: "))

    # Prints a space
    print("")

    # Creates an empty matrix
    matrix = []

    # Fills matrix with 0´s
    for i in range(num_rows):
        matrix.append([])

        for j in range(num_columns):
            matrix[i].append(0)


    # Prints an informative message
    print("(3) Now, it´s time to add some values to your matrix \n")

    # Repeat process until user finishes adding elements to matrix
    while True:
        # User value
        value = input("(3.1) Enter a value for the matrix or QUIT to stop: ")

        if value == "QUIT":
            break;
        else:

            # User´s row location
            row_location = input("(3.2) Enter row location: ")

            if row_location == "QUIT":
                break
            else:
                # While user enters wrong row location
                while not(int(row_location) >= 0 and int(row_location) < num_rows):
                    # Invalid row location
                    print("Hey! That row location is not in the matrix range!")
                    row_location = input("(3.2) Enter row location: ")

                # Valid row location
                row_location = int(row_location)

            # User´s column location
            column_location = input("(3.3) Enter column location: ")

            if column_location == "QUIT":
                break
            else:
                # While user enters wrong column location
                while not(int(column_location) >= 0 and int(column_location) < num_columns):
                    # Invalid column location
                    print("Hey! That column location is not in the matrix range!")
                    column_location = input("(3.3) Enter column location: ")

                # Valid column location
                column_location = int(column_location)

            # Puts user´s value inside matrix (in the place he wants)
            matrix[row_location][column_location] = float(value)

            # Prints a space
            print("")

    # Prints a space
    print("")

    # Prints an informative message
    print("This is your matrix: \n")

    # Prints matrix
    printMatrix(matrix, num_rows, num_columns)

    # Prints a space
    print("")

    # Program´s main loop
    while True:
        # Prints informative messages
        print("(4) What would you like to do? \n")
        print("(4.1) APPLY")
        print("(4.2) TRANSPOSE")
        print("(4.3) PRINT")
        print("(4.4) QUIT")

        # Prints a space
        print("")

        # User input
        user_choice = input("Choice: ")

        # Prints a space
        print("")

        # While user enters invalid option
        while not(user_choice == "4.1" or user_choice == "4.2" or user_choice == "4.3" or user_choice == "4.4"):
            print("Please choose a valid option")
            user_choice = input("Choice: ")
            print("")

        if float(user_choice) == 4.1:

            # User selected APPLY
            print("(5) What would you like to do? \n")
            print("(5.1) SQUARE")
            print("(5.2) MULTIPLY")
            print("")

            # User applu choice
            user_apply_choice = input("Choice: ")

            # While user enters invalid option
            while not(user_apply_choice == "5.1" or user_apply_choice == "5.2"):
                print("")
                print("Please choose a valid option")
                print("")
                user_apply_choice = input("Choice: ")
                print("")

            if user_apply_choice == "5.1":
                # User selected apply square
                print("")

                # Calls applySquare function
                applySquare(matrix, num_rows, num_columns)

                # Prints a space
                print("")

            else:
                # User selected apply multiply

                # Prints a space
                print("")

                # User amount to multiply by
                multiply_number = float(input("Please enter amount to multiply by: "))

                # Prints a space
                print("")

                # Calls applyMultiply function
                applyMultiply(matrix, num_rows, num_columns, multiply_number)

                # Prints a space
                print("")

        elif float(user_choice) == 4.2:
            # User selected TRANSPOSE

            # Calls transpose function that returns transposed matrix
            matrix = transpose(matrix, num_rows, num_columns)

            # Prints a space
            print("")

            # Change num_rows as matrix was transposed
            num_rows = len(matrix)

            # Change num_columns as matrix was transposed
            num_columns = len(matrix[0])

        elif float(user_choice) == 4.3:
            # User selected PRINT
            print("This is your matrix: \n")

            # Calls printMatrix function
            printMatrix(matrix, num_rows, num_columns)

            # Prints a space
            print("")

        else:
            # User selected QUIT

            # Prints ending message
            printEndingMessage()

            break

if __name__ == '__main__':
    main()
