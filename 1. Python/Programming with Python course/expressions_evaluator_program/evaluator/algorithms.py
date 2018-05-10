from evaluator.structures import Stack

# Dictionary d to define operators with higher or equal precedence to a given operator
d = {}

d["^"] = ["^"]
d["*"] = ["^", "*", "/"]
d["/"] = ["^", "*", "/"]
d["+"] = ["^", "*", "/", "+", "-"]
d["-"] = ["^", "*", "/", "+", "-"]

# Convert infix to posfix function
def convert_infix_to_posfix(infix):
    # 1. Operators stack
    O = Stack()

    print("(1.1) Operators stack O created.")
    print("")

    # 2. Input infix string converted to list I

    # List that only identifies 1 digit numbers
    list_only_one_digit_numbers = [x for x in infix]

    # List that will identify more than 1 digit numbers
    I = []

    current_number = ""

    # Algorithm to identify numbers with more than 1 digit
    for counter,value in enumerate(list_only_one_digit_numbers):
        if is_operand(value):
            current_number = current_number + value
        elif is_operator(value):
            if value != "(":
                if value != ")":
                    if current_number != "":
                        I.append(current_number)
                        I.append(value)
                        current_number = ""
                    else:
                        I.append(value)
                else:
                    I.append(current_number)
                    I.append(value)
                    current_number = ""
                    continue
            else:
                I.append(value)
        else:
            I.append(value)

    I.append(current_number)

    print("(1.2) Input infix string converted to list I.")
    print("")

    print(I)
    print("")

    # 3. Output list _OUT
    _OUT = []

    print("(1.3) Output list _OUT created.")
    print("")

    # 4. Scan I from left to right
    print("(1.4) Scanning I from left to right.")
    print("")

    for i in I:
        if is_operand(i):
            print(i + " is operand.")
            _OUT.append(i)
        elif i == "(":
            print("(")
            O.push("(")
        elif i == ")":
            print(")")
            string_stack = O.stack_as_list()

            # Pop O until the corresponding left parenthesis is removed
            for i in string_stack:
                print(i)
                if i != "(":
                    O.pop()
                    _OUT.append(i)
                    continue
                else:
                    break

                break
        elif is_operator(i):
            print(i + " is operator.")

            # Remove operators already on O that have higher or equal precedence and append them to _OUT
            operatorsToDelete = operators_with_higher_or_equal_precedence(i)

            string_stack = O.stack_as_list()

            if len(string_stack) > 0:
                for j in string_stack:
                    if j in operatorsToDelete:
                        _OUT.append(O.pop())

            O.push(i)

    print("")
    print("This is the stack O after scanning I from left to right: ")
    print(O)
    print("")

    print("This is the output list _OUT after scanning I from left to right: ")
    print(_OUT)
    print("")

    # 5. Finished processing input expression. Check O
    print("(1.5) Finished processing input expression. Check O.")
    print("")

    string_stack = O.stack_as_list()

    for i in string_stack:
        O.pop()
        if i != "(":
            _OUT.append(i)

    print("This is the stack O after checking O: ")
    print(O)
    print("")

    print("This is the output list _OUT after checking O: ")
    print(_OUT)
    print("")

    return _OUT

# Returns a list with the operators with higher or equal precedence to i
def operators_with_higher_or_equal_precedence(i):
    return d[i]

# Evaluate posfix function
def evaluate_posfix(posfix):
    # 1. Create stack S for operands
    S = Stack()

    print("(2.1) Stack S for operands created.")
    print("")

    operand_1 = 0
    operand_2 = 0

    # 2. Scan the expression from left to right
    print("(2.2) Scanning the expression from left to right.")
    print("")

    for i in posfix:
        if is_operand(i):
            # The element is a number so it is pushed to S
            print(i + " is an operand")
            S.push(i)
        else:
            # The element is an operator so operands are popped from S
            print(i + " is an operator")
            print("")

            operand_1 = S.pop()
            operand_2 = S.pop()

            answer = 0

            try:
                operand_2 = str(operand_2)
            except ValueError:
                print("Operand is already string")

            try:
                operand_1 = str(operand_1)
            except ValueError:
                print("Operand is already string")

            number_1 = convert_str_to_number(operand_2)
            number_2 = convert_str_to_number(operand_1)

            # Evaluates operator
            if i == "+":
                answer = number_1 + number_2
            elif i == "-":
                answer = number_1 - number_2
            elif i == "*":
                answer = number_1 * number_2
            elif i == "/":
                answer = number_1 / number_2
            elif i == "^":
                answer = number_1 ** number_2

            # The result is pushed to s
            S.push(answer)

    print("")

    print("(2.3) The expression is ended. The final answer is at the top of S.")
    print("")

    # 3. The final answer is at the top of S
    final_answer = S.peek()

    return final_answer

# Returns True if element is an operand and False if it is not
def is_operand(element):
    if not (element == "+" or element == "-" or element == "*" or element == "/" or element == "^" or element == "(" or element == ")"):
        return True
    else:
        return False

# Returns True if element is an operator and False if it is not
def is_operator(element):
    if element == "+" or element == "-" or element == "*" or element == "/" or element == "^" or element == "(" or element == ")":
        return True
    else:
        return False

# Convert string to number function
def convert_str_to_number(string_to_convert):
    # Will have the number
    ans = 0
    
    try:
        dec = string_to_convert.index('.')
    except:
        dec = None

    if dec is None:
        # string_to_convert has no decimal
        for i in string_to_convert:
            ans = ans*10 + ord(i) - ord('0')

        return ans;

    else:
        # string_to_convert has decimal
        print("Converting " + string_to_convert + " to float.")
        print("")

        print("Decimal at position %d" % dec)
        print("")

        # The negative power of the first number to take into account (the number at the right of the string)
        counter = -((len(string_to_convert) - 1) - dec)

        left = False

        for i in reversed(string_to_convert):
            if i == ".":
                counter = 0
                left = True
            elif not left:
                number = ord(i)-ord('0')
                ans = ans + (number * (10 ** counter))
                counter = counter - 1
            elif left:
                if i != " ":
                    number = ord(i)-ord('0')
                    ans = ans + (number * (10 ** counter))
                    counter = counter + 1

        print(string_to_convert + " converted to " + str(ans) + ".")
        print("")

        return ans
