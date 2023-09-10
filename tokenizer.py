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
        output_string = ""

        for i in range(len(self.input)):
            current_char = self.input[i]
            previous_char = self.input[i - 1] if i != 0 else ""

            if current_char == "(" and previous_char.isnumeric(): # multiplying brackets like 5(4 + 3)
                output_string += "*" # so bracket is like 5*(4+3)
            elif current_char.isnumeric() and previous_char == "-": 
                output_string = output_string[:-1] # Removes last character (-) of output
                output_string += "+-"
            elif current_char == previous_char and current_char == "-":
                output_string = output_string[:-1]
                output_string += "+"
                current_char = "" # I don't really like this solution but eh

            # TODO: Fix -- 

            output_string += current_char

        self.input = output_string
        print(f"Formatted input is '{self.input}'")

    # Parses the input into an array of tokens
    def parse_input(self):
        output_list = []

        input_string = self.input
        input_string_length = len(self.input)

        slicing = False
        wasSlicing = False

        i = 0

        while i < input_string_length:
            current_char = input_string[i]
            previous_char = input_string[i - 1]

            print(f"Input string: {input_string} {input_string_length}")
            print(f"i: {i} {current_char}")

            if self.isOperator(current_char):
                output_list.append(Token(TokenType.OPERATOR, current_char))

                # Slice
                input_string = input_string[1:]
                input_string_length = len(input_string)
                i = -1
                slicing = False
            elif self.isNumeric(current_char):
                slicing = True
            else:
                slicing = False
                wasSlicing = True

            if slicing == False and wasSlicing == True:
                wasSlicing = False
                slice = input_string[i:]
                print(slice)

            i += 1

        """
        start_index = 0
        end_index = 0
        
        slicing = False

        openingParentheisCount = 0
        closingParenthesisCount = 0

        for i in range(len(self.input)):
            current_char = self.input[i]
            toAppend = None
            
            if current_char == "(":
                if not slicing:
                    start_index = i
                    end_index = i
                    slicing = True
                
                end_index += 1
                openingParentheisCount += 1
            elif current_char == ")":
                closingParenthesisCount += 1

                if openingParentheisCount == closingParenthesisCount:
                    print(f"end slice {i} {current_char}")
                    print(f"{start_index}   {end_index}")
                    openingParentheisCount = 0
                    closingParenthesisCount = 0
                else:
                    print(f"skipped {i} {current_char}")
                
            elif self.isOperator(current_char):
                toAppend = Token(TokenType.OPERATOR, current_char)
                slicing = False
            elif self.isNumeric(current_char):
                if not slicing:
                    start_index = i
                    end_index = i

                slicing = True
                end_index += 1 

            if i == len(self.input) - 1:
                slicing = False
                slicingParenthesis = False

            if start_index != 0 and end_index != 0 and slicing == False:
                slice = self.input[start_index:end_index]
                output_list.append(Token(TokenType.NUMBER, slice))
                start_index = 0
                end_index = 0

            if toAppend != None:
                output_list.append(toAppend)"""

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
