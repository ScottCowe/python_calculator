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
        #self.format_input()
        self.parse_input()

    def validate_input(self):
        for i in range(len(self.input)):
            current_char = self.input[i]
            
            isOperator = current_char == "+" or current_char == "-" or current_char == "*" or current_char == "/" or current_char == "^" 
            isParenthesis = current_char == "(" or current_char == ")"
            isDecimalPoint = current_char == "."

            if not isOperator and not isParenthesis and not isDecimalPoint and not current_char.isnumeric():
               raise Exception("Input is not valid") 

        print(f"'{self.input}' is valid input")
    
    # Formats input so that a subtraction is an addition of a negative, also cleans up subtracting negatives and multiplying parenthesis
    def format_input(self):
        input_str = self.input
        input_str_length = len(self.input)

        i = 0

        while i < input_str_length:
            current_char = input_str[i]
            next_char = input_str[i+1]

            print(f"{i} {current_char} {input_str}")

            if current_char == "-":
                before = input_str[:i]
                after = input_str[i:]

                input_str = before + "+" + after
                input_str_length = len(input_str)

                i += 1

                if next_char == "-":
                    after = input_str[i+2:]
                    print(input_str)
                    print(before)
                    print(after)

                    input_str = before + "+" + after

                    i -= 1
            i += 1

    # Parses the input into an array of tokens
    def parse_input(self):
        input_str = self.input
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
                
            i += 1

    def treeify(self):
        return None

    def isNumeric(self, string):
        return string.isnumeric() or string == "." or string == "-"

tokenizer = Tokenizer("+123+456")
