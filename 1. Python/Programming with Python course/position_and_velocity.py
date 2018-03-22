# The position and velocity program
# Written by japoveda10

# Print title function
def print_title():
    print("-------------------------------------------------------------")
    print("-               Position and velocity program               -")
    print("-------------------------------------------------------------")

# Print introduction function
def print_introduction():
    print("(1) Introduction \n")

    print("In Kinematics, the motion of an object can be represented by a polynomial.")
    print("For this program, the position equation of an object is going to be represented by: \n")
    print("quadratic_term t^2 + linear_term t + constant_time \n")
    print("The velocity equation is the derivate of the position equation.")
    print("For this program´s position equation, the velocity equation is going to be: \n")
    print("2 * quadratic_term t + linear_term \n")
    print("If we replace the t in both equations by a number, we can obtain the ")
    print("position and velocity of the object represented by the equations in time number you input. \n")

# Function that rounds number 3 digits after comma
def roundNumber(number):

    # number is multiplied by 1000 and casted to int to delete decimal values
    # then the result is divided by 1000 to put point in original position
    numberToTakeIntoAccount = int(number*10000) / 10000

    # This number determines if number will be rounded or not
    lastNumber = str(numberToTakeIntoAccount)[-1]

    # If the number is greater than or equal to 5
    if int(lastNumber) >= 5:
        # Round the number
        roundedNumber = numberToTakeIntoAccount + 0.001
        shorterRoundedNumber = int(roundedNumber*1000) / 1000
    else:
        # Do not round the number
        roundedNumber = numberToTakeIntoAccount
        shorterRoundedNumber = int(roundedNumber*1000) / 1000

    return shorterRoundedNumber

# Print ending message function
def print_ending_message():
    print("-------------------------------------------------------------")
    print("-   Thank you for using the Position and Velocity program   -")
    print("-------------------------------------------------------------")

# Main function
def main():

    # Prints the title
    print_title()

    # Prints a space
    print("")

    # Prints the welcome message
    print("Hello! Welcome to the position and velocity program! \n")

    # Prints introduction
    print_introduction()

    # Prints the instructions message
    print("(2) Instructions \n")
    print("Please enter the following information about the position equation: \n")

    # Declaration, assignment and cast from str to float of constant_term
    unrounded_constant_term = float(input("(2.1) Enter the constant term: "))

    # Rounding constant term using a function I created
    constant_term = roundNumber(unrounded_constant_term)

    # Declaration, assignment and cast from str to float of linear_term
    unrounded_linear_term = float(input("(2.2) Enter the linear term: "))

    # Rounding linear term using a function I created
    linear_term = roundNumber(unrounded_linear_term)

    # Declaration, assignment and cast from str to float of quadratic_term
    unrounded_quadratic_term = float(input("(2.3) Enter the quadratic term: "))

    # Rounding quadratic term using a function I created
    quadratic_term = roundNumber(unrounded_quadratic_term)

    # Position equation definition
    position_equation = str(quadratic_term) + "t^2 + " + str(linear_term) + "t + " + str(constant_term)

    # Velocity equation definition
    velocity_equation = str(int(unrounded_quadratic_term * 2 * 1000) / 1000) + "t + " + str(linear_term)

    # Prints a space
    print("")

    # Position equation output message
    print("The position equation is: " + position_equation)

    # Velocity equation output message
    print("The velocity equation is: " + velocity_equation)

    # Prints a space
    print("")

    # Time entered by the user
    time = float(input("(3) Enter a time to calculate: "))

    # Prints a space
    print("")

    # Math operations to calculate position at time entered by the user
    positionAtTime = roundNumber(unrounded_quadratic_term * (time * time) + (unrounded_linear_term * time) + (unrounded_constant_term))

    # Math operations to calculate velocity at time entered by the user
    velocityAtTime = roundNumber((unrounded_quadratic_term * 2 * time) + unrounded_linear_term)

    # Shorter position at time entered by the user
    shorterPositionAtTime = int(positionAtTime * 1000) / 1000

    # Shorter velocity at time entered by the user
    shorterVelocityAtTime = int(velocityAtTime * 1000) / 1000

    # Position at time entered by the user output message
    print("The position at time " + str(time) + "0" + " is " + str(shorterPositionAtTime))

    # Velocity at time entered by the user output message
    print("The velocity at time " + str(time) + "0" + " is " + str(shorterVelocityAtTime))

    # Prints a space
    print("")

    # Prints ending message
    print_ending_message()

if __name__ == '__main__':
    main()
