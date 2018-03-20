# Sorting lists program
# By japoveda10

# Imports
from random import randint

# Print title function
def print_title():
    print("-----------------------------------------------------------")
    print("-          Welcome to the sorting lists program           -")
    print("-----------------------------------------------------------")

# Print instructions function
def print_instructions():
    print("")
    print("(1) Instructions")
    print("")
    print("This program is going to create two lists of random numbers\n(you define their size) to see how long does it takes to sort them\nusing Python´s sorted function. \n")

# Print ending message function
def print_ending_message():
    print("-----------------------------------------------------------")
    print("-       Thank you for using the sorting lists program     -")
    print("-----------------------------------------------------------")

# Main function
def main():
    # Prints title
    print_title()

    # Prints instructions
    print_instructions()

    # User´s input
    first_list_size = int(input("(1.1) Please enter the first list size: "))
    second_list_size = int(input("(1.2) Please enter the second list size: "))
    print("")

    # Creates two lists
    first_list = []
    second_list = []

    # Fills in first_list
    for i in range(first_list_size):
        first_list.append(randint(0, 10000))

    # Fills in second_list
    for i in range(second_list_size):
        second_list.append(randint(0, 10000))

    print("This is the first list: ")
    print(first_list)
    print("")

    print("This is the second list: ")
    print(second_list)
    print("")

    # Prints ending message
    print_ending_message()

if __name__ == '__main__':
    main()
