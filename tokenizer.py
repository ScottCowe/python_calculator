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
        self.parsed_list = self.parse_input()
        self.validate_array()

    def validate_input(self):
        openingParenthesisCount = 0
        closingParenthesisCount = 0
        
        for i in range(len(self.input)):
            current_char = self.input[i]
            
            isOperator = current_char == "+" or current_char == "-" or current_char == "*" or current_char == "/" or current_char == "^" 
            isParenthesis = current_char == "(" or current_char == ")"
            isDecimalPoint = current_char == "."

            if not isOperator and not isParenthesis and not isDecimalPoint and not current_char.isnumeric():
               raise Exception("Input is not valid")

            if current_char == "(":
                openingParenthesisCount += 1
            elif current_char == ")":
                closingParenthesisCount += 1

        if openingParenthesisCount != closingParenthesisCount:
            raise Exception("Unmatched brackets")

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
                    self.input = before + ("+" if i != 1 else "") + after # This is to deal with negatives at the start of the expression

                    # TODO: Ensure that negatives before brackets are treated as -1 * bracket

                    i += 2
            else:
                i += 1

        print(f"Formatted input is '{self.input}'")

    # Parses the input into an array of tokens
    def parse_input(self):
        output_list = []

        input_string = self.input
        input_string_length = len(self.input)

        slicing = True

        openingBracketCount = 0
        closingBracketCount = 0
        
        i = 0

        while i < input_string_length:
            
            current_char = input_string[i]
            next_char = input_string[i + 1] if i != input_string_length - 1 else ""

            if current_char == "(":
                openingBracketCount += 1
                slicing = True
            elif current_char == ")":
                closingBracketCount += 1
            
            if openingBracketCount > 0:
                if openingBracketCount == closingBracketCount:
                    slicing = False
            elif (self.isNumeric(current_char) != self.isNumeric(next_char)) or (current_char != "(" and next_char == "("):
                slicing = False
            elif next_char == "":
                slicing = False

            if slicing == False:
                before = input_string[0:i+1]
                after = input_string[i+1:]
                slicing = True
                i = -1
                input_string = after
                input_string_length = len(after)

                tokenType = TokenType.EXPRESSION
                if self.isOperator(before[0]):
                    tokenType = TokenType.OPERATOR
                elif self.isNumeric(before[0]):
                    tokenType = TokenType.NUMBER

                output_list.append(Token(tokenType, before))

            i += 1

        print(f"Token values are: ")
        out_str = ""
        for i in range(len(output_list)):
            out_str += output_list[i].value + " "
        print(out_str)

        return output_list

    def validate_array(self):
        for i in range(len(self.parsed_list)):
            current_token_type = self.parsed_list[i].type
            if i % 2 != 0: # Is odd
                if current_token_type != TokenType.OPERATOR:
                    raise Exception("Input is not correctly ordered")
            else: # Is even, should be expression or number
                if current_token_type == TokenType.OPERATOR:
                    raise Exception("Input is not correctly ordered")
        
        print("Array is ordered correctly")

    def isOperator(self, char):
        return char == "+" or char == "*" or char == "/" or char == "^"

    def isNumeric(self, char):
        return char.isnumeric() or char == "." or char == "-"

tokenizer = Tokenizer("-123--456(45 + 3)")
