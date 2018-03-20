# Sorting lists program
# By japoveda10

# Imports
import time
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
    print("This program is going to create two lists of random numbers\n(you define their size) to see how much time does Python´s\nsorted function takes to sort the lists.\n")

def sort_lists(first_list, second_list):
    print("")
    print("(3) Time comparison")
    print("")

    # First list

    # Start time
    first_list_start_time = time.time()

    # Sort first_list
    first_list_sorted = sorted(first_list)

    # End time
    first_list_end_time = time.time()

    # Informative message
    print("(3.1) Python´s sorted function took " + str(first_list_end_time - first_list_start_time) + " to sort the first list.")

    # Second list

    # Start time
    second_list_start_time = time.time()

    # Sort first_list
    second_list_sorted = sorted(second_list)

    # End time
    second_list_end_time = time.time()

    # Informative message
    print("(3.2) Python´s sorted function took " + str(second_list_end_time - second_list_start_time) + " to sort the second list.")

    print("")

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

    print("")
    print("(2) Your lists")
    print("")

    print("(2.1) This is the first list: ")
    print(first_list)
    print("")

    print("(2.2) This is the second list: ")
    print(second_list)
    print("")

    # Sorts lists and calculates times
    sort_lists(first_list, second_list)

    # Prints ending message
    print_ending_message()

if __name__ == '__main__':
    main()
