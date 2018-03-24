# The grade book program
# Written by japoveda10

# Print title function
def print_title():
    print("----------------------------------------------")
    print("-          Welcome to the grade book         -")
    print("----------------------------------------------")

# Print instructions function
def print_instructions():
    print("What would you like to do? \n")
    print("(1) New Student")
    print("(2) Search Students")
    print("(3) Enter Grade")
    print("(4) Add Assignment")
    print("(5) Delete Assignment")
    print("(6) Print All Students Information")
    print("(7) Quit")

# New student function
def new_student(students_dictionary, assignments):
    # Prints a space
    print("")
    print("(1.1) Please enter the following information: ")
    print("")

    student_name = input("Student name: ")

    # Enter the if statement block if the dictionary is not empty
    if len(students_dictionary) > 0:
        # Check if student already exists
        while True:
            try:
                if (students_dictionary[student_name] != None):
                    # Student already exist
                    print("")
                    print("Student already exist. Type another name please. \n")
                    student_name = input("Student name: ")
            except Exception as e:
                # Student does not exist
                break

    while True:
        try:
            student_age = int(input("Student age: "))
            break
        except ValueError:
            # User did not enter a number
            print("")
            print("Please enter a number for the age. \n")

    student_address = input("Student address: ")
    print("")

    # Adds student to the students_dictionary, student_name is the key for the student
    students_dictionary[student_name] = [student_age, student_address, assignments]

    # Informative message
    print("Student was successfully added \n")

# Search student function
def search_student(students_dictionary):
    # Prints a space
    print("")
    student_name = input("(2.1) Please enter student name or prefix: ")
    print("")

    # List of searched students
    searched_students = []

    # Iterate through students_dictionary to add elements to searched_student
    for key, value in students_dictionary.items():
        # The student´s name starts with student_name?
        if(key.startswith(student_name)):
            searched_students.append(key)

    # Is searched_students empty?
    if len(searched_students) == 0:
        print("There are no students with the name or prefix " + student_name)
        print("")
    else:
        for i in searched_students:
            # searched_student has all information about a student i
            searched_student = students_dictionary[i]

            # Prints student name
            print(i)

            # Prints all information about student i
            for j in searched_student:
                print("\t" + str(j))

            print("")

# Add assignment function
def add_assignment(students_dictionary, assignments):
    # Prints a space
    print("")
    assignment_name = input("Please enter the name of the assignment: ")

    # While assignment_name already is inside assignments
    while assignment_name in assignments.keys():
        print("")
        print("The assignment already exists")
        print("")
        assignment_name = input("Please enter the name of the assignment: ")

    # Creates new assignment
    assignments[assignment_name] = "-"

    # Updates information for every student
    for key, value in students_dictionary.items():
        student_age = value[0]
        student_address = value[1]
        student_assignments = value[2]
        student_assignments[assignment_name] = "-"
        students_dictionary[key] = [student_age, student_address, student_assignments]

    # Informative message
    print("Assignment added")

    # Prints students information
    print_students(students_dictionary)

# Enter grade function
def enter_grade(students_dictionary, assignments):
    # Prints a space
    print("")

    if len(students_dictionary) == 0:
        print("There are no students to grade")
        print("")
    elif len(assignments) == 0:
        print("There are no assignments")
        print("")
    else:
        # User´s input
        student_name = input("Please enter student name: ")

        # While user enters a student name that does not exist
        while not (student_name in students_dictionary.keys()):
            print("The student does not exist")
            student_name = input("Please enter student name: ")

        # User´s input
        assignment_name = input("Please enter assignment name: ")

        # While user enter an assignment name that does not exist
        while not (assignment_name in assignments.keys()):
            print("The assignment does not exist")
            assignment_name = input("Please enter assignment name: ")

        while True:
            try:
                # User´s input
                assignment_grade = int(input("Please enter assignment grade: "))

                # Is the grade valid?
                if assignment_grade >= 0 and assignment_grade <= 100:
                    break
                else:
                    # The grade is not valid
                    print("The grade must be a number between 0 and 100")
                    continue
            except ValueError:
                # The grade is not valid because it is not a number
                print("")
                print("The grade must be a number between 0 and 100")
                print("")

        # Student age
        student_age = students_dictionary[student_name][0]

        # Student adress
        student_address = students_dictionary[student_name][1]

        # Student assignments
        student_assignments = students_dictionary[student_name][2]

        # assignment_name graded
        student_assignments[assignment_name] = assignment_grade

        # Data updated to students_dictionary
        students_dictionary[student_name] = [student_age, student_address, student_assignments]

        # Informative message
        print("Grade assigned for " + assignment_name.upper() + ".")

        # Prints students information
        print_students(students_dictionary)

# Delete assignment
def delete_assignment(students_dictionary, assignments):
    # Prints a space
    print("")

    # User input
    assignment_to_delete = input("Please enter the name of the assignment to delete: ")

    # While user input is not an assignment
    while not (assignment_to_delete in assignments.keys()):
        print("")
        print("The assignment does not exist")
        print("")
        assignment_to_delete = input("Please enter the name of the assignment to delete")

    # User input is an existing assignment

    # Deletes assignment
    del assignments[assignment_to_delete]

    # Prints students information
    print_students(students_dictionary)

# Print students information function
def print_students(students_dictionary):
    for key, value in students_dictionary.items():
        print(key, value)

# Print ending message function
def print_ending_message():
    print("----------------------------------------------")
    print("-     Thank you for using the grade book     -")
    print("----------------------------------------------")

# Main function
def main():
    # Prints title
    print_title()

    # Prints a space
    print("")

    # Students dictionary
    students_dictionary = {}

    # Assignmnets model
    assignments = {}

    while True:
        # Prints instructions
        print_instructions()

        # Prints a space
        print("")

        # User choice
        user_choice = input("Your choice: ")

        # While user writes invalid option
        while not(user_choice == "1" or user_choice == "2" or user_choice == "3" or user_choice == "4" or user_choice == "5" or user_choice == "6" or user_choice == "7"):
            print("")
            print("Please type a valid option")
            print("")
            user_choice = input("Your choice: ")

        # User wrote valid option
        if user_choice == "1":
            # New student
            new_student(students_dictionary, assignments)
        elif user_choice == "2":
            # Search student
            search_student(students_dictionary)
        elif user_choice == "3":
            # Enter grade
            enter_grade(students_dictionary, assignments)
        elif user_choice == "4":
            # Add Assigmnet
            add_assignment(students_dictionary, assignments)
        elif user_choice == "5":
            # Delete assignment
            delete_assignment(students_dictionary, assignments)
        elif user_choice == "6":
            # Print students_dictionary
            print_students(students_dictionary)
        else:
            print("")
            print_ending_message()
            break

if __name__ == '__main__':
    main()
