# Class that represents a Stack
class Stack():

    # Constructor
    def __init__(self):
        self.elements = []

    # Adds element to the top stack
    def push(self, element):
        self.elements.append(element)

    # Deletes the top of the stack
    def pop(self):
        return self.elements.pop()

    # Returns the element that is at the top of the stack
    def peek(self):
        return self.elements[len(self.elements) - 1]

    # Returns the size of the stack
    def size(self):
        return len(self.elements)

    # Returns True if the stack is empty or False if it is not
    def is_empty(self):
        return len(self.elements) == 0

    # Prints stack as a string
    def __str__(self):
        answer = ""
        reversed_elements = list(reversed(self.elements))
        for i in reversed_elements:
            answer += str(i) + "\n"

        return answer

    # Returns stack as a list
    def stack_as_list(self):
        answer = ""
        reversed_elements = list(reversed(self.elements))
        for i in reversed_elements:
            answer += str(i)

        return answer
