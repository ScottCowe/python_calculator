from enum import Enum

class TokenType(Enum):
    NUMBER = 1
    OPERATOR = 2

class Token():
    def __init__(self, token_type, value):
        self.token_type = token_type
        self.value = value

class Tokenizer():
    def __init__(self, input_string):
        self.input_string = input_string.replace(" ", "")

        self.first_pass()
        print("First pass completed")
        self.second_pass()
        print("Second pass completed")
        print(self.input_string)
        # First pass: check for invalid characters
        # Second pass: convert - into + - and turn resulting -- into +
        # Third pass: gets all numbers and operaters and adds them to the tokens array
            # It does this by taking all - or numeric chars as the start of numbers, then the end as a number. '.'s are allowed

    def first_pass(self):
        for i in range(len(self.input_string)):
            current_char = self.input_string[i]

            # Using the term operator here is technically incorrect, as it also checks for '.' and brackets
            operator = True
            number = current_char.isnumeric()

            # If char is not a number or operator, exit program
            if current_char != "+" and current_char != "-" and current_char != "*" and current_char != "/" and current_char != "^" and current_char != "." and current_char != "(" and current_char != ")":
                operator = False

            if not operator and not number:
                raise Exception("Expression contained invalid characters")

    def second_pass(self):
        # Input string length must be constantly reevaluated
        input_length = len(self.input_string)
        i = 0
        while i < input_length:
            current_char = self.input_string[i]
            # Convert - into +-
            #   Split string into before index of - and after
            #   Put string back together

            if current_char == "-":
                before = self.input_string[:i]
                after = self.input_string[i+1:]
                self.input_string = before + "+-" + after
                input_length = len(self.input_string)
                i += 1

                next_char = self.input_string[i+1]

                # If --
                if current_char == next_char:
                    before = self.input_string[:i-1]
                    after = self.input_string[i+2:]
                    self.input_string = before + "+" + after
                    input_length = len(self.input_string)
                    
            i += 1        
                    
        # Idea: take subtraction as addition plus a negative (5 - 4 => 5 + -4)

        # Iterate through string
        # First element must be number or bracket, or -
        #   If first element is number, iterate thru string until an operator, then set the first token to the number (ex 54.25)
        #   If first element is a bracket, iterate through until the closing bracket is found
        #       This is done by having a counter of opening brackets '(', and when another opening bracket is found, the counter is incremented
        #       When a closing bracket is found ')', the counter is decremented. When the counter is 0, then the entire expression inside the bracket can be evaluated
        #           This is done by tokenizing the expression inside the bracket, then evaluating it, and setting the next token to a number with its value

    def get_tokens(self):
        return self.token_tree # What fun, i've never even worked with trees before

class OperatorType(Enum):
    ADDITION = "+"
    SUBTRACTION = "-"
    MULTIPLICATION = "*"
    DIVISION = "/"
    EXPONENTIATON = "^"

class Evaluator():
    def __init__(self, number1, number2, operator):
        self.number1 = number1
        self.number2 = number2
        self.operator = operator

    def evaluate(self):
        # Perform action based on operator
        return 0

tokenizer = Tokenizer("54-67--193 + 1")
