from enum import Enum

class TokenType(Enum):
    NUMBER = 0
    OPERATOR = 1

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

            output_string += current_char

        self.input = output_string
        print(f"Formatted input is '{self.input}'")

    # Parses the input into an array of tokens
    def parse_input(self):
        """input_str = self.input
        input_str_length = len(self.input)
        end_index = 0

        i = 0

        isNumeric = False
        isOperator = False
        isParenthesis = False

        while i < input_str_length:
            current_char = input_str[i]
            isNumeric = self.isNumeric(current_char)
            isOperator = current_char == "+" or current_char == "*" or current_char == "/" or current_char == "^"
            isParenthesis = current_char == "(" or current_char == ")"

            print(f"Input string: {input_str}")
            print(f"{i} {current_char}")
            print(f"{isNumeric} {isOperator} {isParenthesis}")

            if isOperator:
                self.tokens.append(Token(TokenType.OPERATOR, current_char))
                after = input_str[1:]
                input_str = after
                input_str_length = len(after)
                i = -1
            elif isNumeric:
                if i == input_str_length - 1: # At end of string
                    self.tokens.append(Token(TokenType.NUMBER, input_str))
                    print("end")

                    for i in range(len(self.tokens)):
                        print(self.tokens[i].value)
                elif self.isNumeric(input_str[i + 1]): # Next char is numeric
                    end_index += 1
                    print("incremented end index")
                else:
                    print(f"End index is {end_index}")
                    print(f"Char at end index is {input_str[end_index]}")
                    before = input_str[:end_index + 1]
                    after = input_str[end_index + 1:]
                    self.tokens.append(Token(TokenType.NUMBER, before))
                    input_str = after
                    input_str_length = len(after)
                    i = -1
                
            i += 1"""
        
        output_list = []

        start_index = 0
        end_index = 0
        
        slicing = False

        for i in range(len(self.input)):
            current_char = self.input[i]
            toAppend = None

            if self.isOperator(current_char):
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

            if start_index != 0 and end_index != 0 and slicing == False:
                slice = self.input[start_index:end_index]
                output_list.append(Token(TokenType.NUMBER, slice))
                start_index = 0
                end_index = 0

            if toAppend != None:
                output_list.append(toAppend)

        print(f"Token values are: ")
        for i in range(len(output_list)):
            print(output_list[i].value)

    def treeify(self):
        return None

    def isOperator(self, char):
        return char == "+" or char == "*" or char == "/" or char == "^"

    def isNumeric(self, char):
        return char.isnumeric() or char == "." or char == "-"

tokenizer = Tokenizer("+123--456")
