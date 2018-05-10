# The grade book program version 2
# Written by japoveda10

# Student class
class Student():
    # Class constructor
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        self.assignments = {}

# Assignment class
class Assignment():
    # Class constructor
    def __init__(self, assignment_name):
        self.assignment_name = assignment_name
        self.grade = "-"

# Prints title
def print_title():
    print("----------------------------------------------------")
    print("-        Welcome to the grade book version 2       -")
    print("----------------------------------------------------")

# Prints instructions
def print_instructions():
    print("What would you like to do? \n")
    print("(1) New Student")
    print("(2) Search Student")
    print("(3) Enter Grade")
    print("(4) Add Assignment")
    print("(5) Delete Assignment")
    print("(6) Print All Students Information")
    print("(7) Quit")

# Add student function
def add_student(students_db, assignments):
    # Informative message
    print("(1.1) Please enter the following information: ")

    # Prints a space
    print("")

    # Student name
    student_name = input("Student name: ")

    # Check if student already exists
    while True:
        if(student_name in students_db.keys()):
            print("")
            print("The student already exists")
            print("")
            student_name = input("Student name: ")
        else:
            break

    # Checks that age is a number
    while True:
        try:
            # Student age
            student_age = int(input("Student age: "))
            break
        except ValueError:
            # User did not enter a number
            print("")
            print("Please enter a number for the age. \n")

    # Student address
    student_address = input("Student address: ")

    # Prints a space
    print("")

    # Creates instance of class Student
    student = Student(student_name, student_age, student_address)

    # Adds student to db
    students_db[student_name] = student

    # Are there assignments we need to create for this student?
    if (len(assignments) > 0):
        for i in assignments:
            # student has all information about student student_name
            student = students_db[student_name]

            # Creates new assignment
            new_assignment = Assignment(i)
            student.assignments[i] = new_assignment

    print(student_name + " was successfully added.")

# Search student function
def search_student(students_db):
    # Is the db empty?
    if (len(students_db) == 0):
        print("There are no students")
    else:
        # There are students in the db

        # Student name to find
        student_name = input("(2.1) Please enter student name or prefix: ")

        # Prints a space
        print("")

        # List of searched students
        searched_students = []

        # Iterate through students_db to add elements to searched_students
        for key, value in students_db.items():
            # The student´s name starts with student_name?
            if(key.startswith(student_name)):
                searched_students.append(key)

        # Is searched_students empty?
        if len(searched_students) == 0:
            print("There are no students with that name or prefix")
            print("")
        else:
            # There are students with that name or prefix

            for i in searched_students:
                # searched_student has all information about a student i
                searched_student = students_db[i]

                # Dictionary with contents of object
                attributes = vars(searched_student)

                # Prints student name
                print(i)

                # Prints the each of the object´s attributes and values
                for key, value in attributes.items():
                    if (key != "assignments"):
                        print("\t" + str(key) + ": " + str(value))
                    else:
                        # Prints "assignments"
                        print("\t" + str(key) + ": ")

                        # assignments_dictionary has assignment info
                        assignments_dictionary = value

                        # For each element
                        for j in assignments_dictionary.keys():
                            # Prints assignment name
                            print("\t" + "\t" + "- " + j)
                            assignment = assignments_dictionary[j]
                            attributes_of_assignment = vars(assignment)

                            for key, value in attributes_of_assignment.items():
                                print("\t" + "\t" + str(key) + ": " + str(value))

                            print("")

                # Prints a space
                print("")

# Enter grade function
def enter_grade(students_db, assignments):
    # Is the db empty?
    if (len(students_db) == 0):
        print("There are no students")
    else:
        if (len(assignments) == 0):
            print("There are no assignments")
        else:
            # There are asssignments

            # Informative message
            print("(3.1) Please enter the following information")
            print("")

            # User´s input
            student_name = input("Student name: ")

            # While user enters a student name that does not exist
            while not (student_name in students_db.keys()):
                print("")
                print("The student does not exist")
                print("")
                student_name = input("Please enter an existing student name: ")

            # User´s input
            assignment_name = input("Assignment name: ")

            # While user enter an assignment name that does not exist
            while not (assignment_name in assignments):
                print("")
                print("The assignment does not exist")
                print("")
                assignment_name = input("Please enter an existing assignment name: ")

            while True:
                try:
                    # User´s input
                    assignment_grade = int(input("Assignment grade: "))

                    # Is the grade valid?
                    if assignment_grade >= 0 and assignment_grade <= 100:
                        break
                    else:
                        # The grade is not valid

                        print("")
                        print("The grade must be a number between 0 and 100")
                        print("")

                        continue
                except ValueError:
                    print("")
                    print("The grade must be a number between 0 and 100")
                    print("")

            # student has all information about student student_name
            student = students_db[student_name]

            # Assignment to grade object
            assignment_to_grade = student.assignments[assignment_name]

            # Dictionary with assignment to grade info
            more_clear_assignment_to_grade = vars(assignment_to_grade)

            # Grades assignment
            more_clear_assignment_to_grade["grade"] = assignment_grade

            print("")
            print(assignment_name + " was successfully graded for " + student_name + ".")
            print("")

# Add assignment function
def add_assignment(students_db, assignments):
    # Is the db empty?
    if (len(students_db) == 0):
        print("There are no students")
    else:
        # There are students

        # Informative message
        print("(4.1) Please enter the following information")
        print("")

        # User input
        assignment_name = input("Name of the new assignment: ")

        # While assignment_name is inside assignments
        while assignment_name in assignments:
            print("")
            print("The assignment already exists")
            print("")
            assignment_name = input("Please enter the name of the new assignment: ")

        # Creates assignment for every student
        for i in students_db.keys():
            # student has all information about student i
            student = students_db[i]

            # Creates new assignment
            new_assignment = Assignment(assignment_name)
            assignments.append(assignment_name)

            student.assignments[assignment_name] = new_assignment

        # Prints a space
        print("")

        # Informative message
        print(assignment_name + " was successfully added.")

        # Prints a space
        print("")

# Delete assignment function
def delete_assignment(students_db, assignments):
    # Are there students?
    if (len(students_db) == 0):
        print("There are no students")
    else:
        # Are there assignments?
        if (len(assignments) == 0):
            print("There are no assignments")
        else:
            # There are asssignments

            # Informative message
            print("(5) Please enter the following information: ")
            print("")

            # User input
            assignment_to_delete = input("Assignment to delete: ")

            # While user input is not an assignment
            while not (assignment_to_delete in assignments):
                print("")
                print("The assignment does not exist")
                print("")
                assignment_to_delete = input("Please enter an existing assignment to delete it: ")

            # Deletes assignment for every student
            for i in students_db.keys():
                # student has all information about student i
                student = students_db[i]

                # Dictionary with contents of object
                attributes = vars(student)

                for key, value in attributes.items():
                    if (key == "assignments"):
                        assignments_dictionary = value

                        del assignments_dictionary[assignment_to_delete]

            # Deletes assignment from assignments list
            assignments.remove(assignment_to_delete)

            print("")
            print(assignment_to_delete + " was successfully deleted.")
            print("")

# Print all students information function
def print_all_students_information(students_db):
    # Is the db empty?
    if (len(students_db) == 0):
        print("There are no students")
    else:
        for i in students_db.keys():
            print(i)

            # student has all information about student i
            student = students_db[i]

            # Dictionary with contents of object
            attributes = vars(student)

            # Prints the each of the object´s attributes and values
            for key, value in attributes.items():
                if (key != "assignments"):
                    print("\t" + str(key) + ": " + str(value))
                else:
                    # Prints "assignments"
                    print("\t" + str(key) + ": ")

                    # assignments_dictionary has assignment info
                    assignments_dictionary = value

                    # For each element
                    for j in assignments_dictionary.keys():
                        # Prints assignment name
                        print("\t" + "\t" + "- " + j)
                        assignment = assignments_dictionary[j]
                        attributes_of_assignment = vars(assignment)

                        for key, value in attributes_of_assignment.items():
                            print("\t" + "\t" + str(key) + ": " + str(value))

                        print("")

            # Prints a space
            print("")

# Print ending message
def print_ending_message():
    print("----------------------------------------------------")
    print("-   Thank you for using the grade book version 2   -")
    print("----------------------------------------------------")

# Main function
def main():
    # Prints title
    print_title()

    # Students db
    students_db = {}

    # Assignments
    assignments = []

    # Prints a space
    print("")

    # Main while
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

        # Prints a space
        print("")

        if user_choice == "1":
            # New student
            add_student(students_db, assignments)

            # Prints a space
            print("")
        elif user_choice == "2":
            # Search student
            search_student(students_db)

            # Prints a space
            print("")
        elif user_choice == "3":
            # Enter grade
            enter_grade(students_db, assignments)

            # Prints a space
            print("")
        elif user_choice == "4":
            # Add Assigmnet
            add_assignment(students_db, assignments)

            # Prints a space
            print("")
        elif user_choice == "5":
            # Delete assignment
            delete_assignment(students_db, assignments)

            # Prints a space
            print("")
        elif user_choice == "6":
            # Print students_dictionary
            print_all_students_information(students_db)

            # Prints a space
            print("")
        else:
            print_ending_message()
            break

if __name__ == '__main__':
    main()
