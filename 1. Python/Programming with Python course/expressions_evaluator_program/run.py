# Expressions evaluator program
# Written by japoveda10

import sys
from evaluator import algorithms

# Print title function
def print_title():
    print("--------------------------------------------------------")
    print("-     Welcome to the Expressions evaluator program     -")
    print("--------------------------------------------------------")
    print("")

# Print ending message function
def print_ending_message():
    print("--------------------------------------------------------")
    print("-           Thank you for using our program            -")
    print("--------------------------------------------------------")
    print("")

# Main function
def main(arguments):
    print_title()

    print("You entered " + arguments)
    print("")

    print("--------------------------------------------------------")
    print("(1) Convert infix to posfix")
    print("--------------------------------------------------------")
    print("")

    posfix = algorithms.convert_infix_to_posfix(arguments)

    print("--------------------------------------------------------")
    print("The posfix is: " + str(posfix))
    print("--------------------------------------------------------")
    print("")

    print("--------------------------------------------------------")
    print("(2) Evaluate posfix")
    print("--------------------------------------------------------")
    print("")

    answer = algorithms.evaluate_posfix(posfix)

    print("--------------------------------------------------------")
    print("The answer is: " + arguments + " = " + str(answer))
    print("--------------------------------------------------------")
    print("")

    print_ending_message()

if __name__ == '__main__':
    # Join the user's command arguments and deletes whitespaces
    arguments = ''.join(sys.argv[1:]).replace(" ", "")

    if (len(arguments) == 0):
        # User did not provide expression
        print("Must provide expression.")
    else:
        # User provided expression
        main(arguments)
