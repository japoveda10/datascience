# The slot machine program
# Written by japoveda10

# Imports
from random import randint

# Print title function
def print_title():
    print("-------------------------------------------------------------")
    print("-            Welcome to the slot machine program            -")
    print("-------------------------------------------------------------")

# Print instructions function
def print_instructions():
    print("(1) Instructions \n")
    print("The program will generate 3 random numbers from 1 to 10. These are the scoring ")
    print("rules: \n")
    print("    (1.1) If you obtain three 7´s, you receive 750 points")
    print("    (1.2) If you obtain three numbers that are the same, you receive 250 points")
    print("    (1.3) If you obtain two 7´s, you receive 100 points")
    print("    (1.4) If you obtain two numbers that are the same, you receive 50 points")
    print("    (1.5) If you obtain one 7, you receive -10 points")
    print("    (1.6) If you obtain three distinct numbers, you receive -20 points")

# Get random digit function
def get_random_digit():
    return randint(1, 10)

# Print ending message function
def print_ending_message():
    print("-------------------------------------------------------------")
    print("-        Thank you for using the slot machine program       -")
    print("-------------------------------------------------------------")

# Main function
def main():

    # Prints the title
    print_title()

    # Prints a space
    print("")

    # Prints the welcome message
    print("Hello! Welcome to the slot machine program! \n")

    # Prints the instructions
    print_instructions()

    # Prints a space
    print("")

    # Asks the user if they want to play
    print("Would you like to play? \n")

    # User input
    want_to_play = input("Enter yes/no: ").upper()

    # While the user enters an invalid command
    while not(want_to_play == "YES" or want_to_play == "NO"):
        print("")
        print("Hey! that is not a valid command! \n")
        want_to_play = input("Enter yes/no: ").upper()

    # The user wants to play?
    if want_to_play == "YES":
        # User wants to play

        # Prints a space
        print("")

        # Prints a message
        print("Great! \n")

        # Prints informative message
        print("Generating your three numbers... \n")

        # First random number
        random_num_one = get_random_digit()

        # Second random number
        random_num_two = get_random_digit()

        # Third random number
        random_num_three = get_random_digit()

        # Prints informative message
        print("You spun: " + str(random_num_one) + " " + str(random_num_two) + " " + str(random_num_three) + "\n")

        # Scoring logic

        score = 0

        if random_num_one == random_num_two == random_num_three == 7:
            score = 750
        elif random_num_one == random_num_two == random_num_three:
            score = 250
        elif random_num_one == random_num_two == 7 or random_num_one == random_num_three == 7 or random_num_two == random_num_three == 7:
            score = 100
        elif random_num_one == random_num_two or random_num_one == random_num_three or random_num_two == random_num_three:
            score = 50
        elif random_num_one == 7 or random_num_two == 7 or random_num_three == 7:
            score = -10
        elif random_num_one != random_num_two != random_num_three:
            score = -20

        # If the user score is positive
        if score > 0:
            # Print a positive message
            print("Yay! :) \n")
        else:
            # Print a negative message
            print("Oh no! :( \n")

        # Print the user final score
        print("You received " + str(score) + " points! \n")

        # Prints ending message
        print_ending_message()

        # Prints a space
        print("")

    else:
        # User does not want to play
        print("")

        print("Goodbye \n")

if __name__ == '__main__':
    main()
