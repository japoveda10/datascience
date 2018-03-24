# Dictionary program
# Written by Jamie Anderson and japoveda10

# Prints welcome title
def welcome_title():
    print("----------------------------------------------------")
    print("             Welcome to the dictionary              ")
    print("----------------------------------------------------")

# Prints instructions
def print_instructions():
    print("What would you like to do?")
    print("(1) Find a word")
    print("(2) Print dictionary")
    print("(3) Exit")

# Looks for word search_for inside my_dictionary
def look_for_word(search_for, my_dictionary):
    try:
        # List with words with the same beginning letter as search_for
        words_with_same_beginning_letter = my_dictionary[search_for[0]]

        # Boolean value that says if search_for is inside my_dictionary
        inside_dictionary = search_for in words_with_same_beginning_letter

        if inside_dictionary:
            print(search_for + " is inside the dictionary!")
        else:
            print(search_for + " is not inside the dictionary")

    except Exception as e:
        print(search_for + " is not inside the dictionary")

# Prints my_dictionary
def print_dictionary(my_dictionary):
    for key, value in my_dictionary.items():
        print(key, value)

# Prints exit message
def exit_message():
    print("----------------------------------------------------")
    print("           Thank you for using our program          ")
    print("----------------------------------------------------")

# Main function
def main():
    # Prints welcome title
    welcome_title()

    # Read the file
    with open("words.txt", 'r') as f:
        data = f.readlines()
        data = [x.strip() for x in data]

    # Build dictionary
    my_dictionary = {}

    # Creates list that will have beginning letters in words
    letters = []

    # Fills in letters list
    for i in data:
        letter = i[0]

        # For the first letter to be added
        if len(letters) == 0:
            letters.append(letter)
        else:
            if not(letter in letters):
                letters.append(letter)
            else:
                continue

    # Fills in dictionary
    for i in letters:
        # List created for each letter
        list_for_letter = []
        for j in data:
            if j[0] == i:
                list_for_letter.append(j)
        my_dictionary[i] = list_for_letter

    # Main while loop
    while True:
        # Print instructions
        print_instructions()

        # User´s choice
        user_choice = input("Your choice: ")

        if (user_choice == "1"):
            # Find a word inside my_dictionary
            search_for = input("Type a word you would like to find: ")
            look_for_word(search_for, my_dictionary)
        elif (user_choice == "2"):
            # Print dictionary
            print_dictionary(my_dictionary)
        elif (user_choice == "3"):
            # Exit
            exit_message()
            break
        else:
            # Invalid option
            print("Hey! Type a valid option please")
            continue

if __name__ == '__main__':
    main()
