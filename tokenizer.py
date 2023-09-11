from enum import Enum

class TokenType(Enum):
    NUMBER = 0
    OPERATOR = 1
    EXPRESSION = 2

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

class Tokenizer:
    def __init__(self, input):
        self.input = input.replace(" ", "") # Removes whitespace

        self.tokens = []

        self.validate_input()
        self.format_input()
        self.parse_input()

    def validate_input(self):
        for i in range(len(self.input)):
            current_char = self.input[i]
            
            isOperator = current_char == "+" or current_char == "-" or current_char == "*" or current_char == "/" or current_char == "^" 
            isParenthesis = current_char == "(" or current_char == ")"
            isDecimalPoint = current_char == "."

            if not isOperator and not isParenthesis and not isDecimalPoint and not current_char.isnumeric():
               raise Exception("Input is not valid")

            # TODO: Check if every parenthesis closes
            # TODO: Ensure that operators do not repeat

        print(f"'{self.input}' is valid input")
    
    # Formats input so that a subtraction is an addition of a negative, also cleans up subtracting negatives and multiplying parenthesis
    def format_input(self):
        length = len(self.input)

        i = 0

        while i < length:
            current_char = self.input[i]
            previous_char = self.input[i - 1] if i > 0 else ""

            if current_char == "(" and previous_char.isnumeric():
                before = self.input[0:i]
                after = self.input[i:]
                self.input = before + "*" + after
                length = len(self.input)
                i += 2
            elif self.isNumeric(current_char) and previous_char == "-":
                if current_char == "-":
                    before = self.input[0:i-1]
                    after = self.input[i+1:]
                    self.input = before + "+" + after
                    i += 1
                else:
                    before = self.input[0:i-1]
                    after = self.input[i-1:]
                    self.input = before + "+" + after
                    i += 2
            else:
                i += 1

        print(f"Formatted input is '{self.input}'")

    # Parses the input into an array of tokens
    def parse_input(self):
        output_list = []

        input_string = self.input
        input_string_length = len(self.input)

        slicing = False

        openingBracketCount = 0
        closingBracketCount = 0
        
        i = 0

        while i < input_string_length:
            current_char = input_string[i]]
            next_char = input_string[i + 1] if i < input_string_length else ""
            
            # Check if slicing should stop
            #     If openingBracketCount > 0
            #         
            #     If current char and next char are different types, stop      
            #     If next char does not exist, stop
            #     Else continue
            
            # If slicing has stopped, get slice, and add to token list
            #     Check type of slice and create corrosponding token
            #     Remove slice from startof input_string and update length
            #     Set i to 0
            #     Start slicing

            i += 1

        print(f"Token values are: ")
        for i in range(len(output_list)):
            print(output_list[i].value)

    def treeify(self):
        return None

    def isOperator(self, char):
        return char == "+" or char == "*" or char == "/" or char == "^"

    def isNumeric(self, char):
        return char.isnumeric() or char == "." or char == "-"

tokenizer = Tokenizer("+123--456(45 + 3)")
