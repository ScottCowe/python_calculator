from enum import Enum
from tokenizer import *

class Operator():
    def __init__(self, as_char):
        self.as_char = as_char
        self.type = None
        self.priority = 0

        match as_char:
            case "+":
                self.type = OperatorType.ADDITION
                self.priority = 1
            case "*":
                self.type = OperatorType.MULTIPLICATION
                self.priority = 2
            case "/":
                self.type = OperatorType.DIVISION
                self.priority = 2
            case "^":
                self.type = OperatorType.EXPONENTIATION
                self.priority = 3

class OperatorType(Enum):
    ADDITION = 0
    MULTIPLICATION = 1
    DIVISION = 2
    EXPONENTIATION = 3

class Expression:
    def __init__(self, operator, left, right):
        self.operator = operator
        self.left = left
        self.right = right

    def evaluate(self):
        match self.operator.type:
            case OperatorType.ADDITION:
                return float(self.left) + float(self.right)
            case OperatorType.MULTIPLICATION:
                return float(self.left) * float(self.right)
            case OperatorType.DIVISION:
                return float(self.left) / float(self.right)
            case OperatorType.EXPONENTIATION:
                return float(self.left) ** float(self.right)

class Evaluator():
    def __init__(self, array_expression):
        self.array_expression = array_expression

    def evaluate(self):
        input_array = self.array_expression

        for i in range(0, len(input_array)):
            if input_array[i].type == TokenType.EXPRESSION:
                print()
                # Refactor code using dep injection
        
        # for each bracket in array
        #   parse using tokenizer
        #   recursively evaluate until answer is found
        #   sub answer into array in place of bracket

        # for all exponentials from left to right
        #   evaluate exponential and sub into array
        # for all multiplication and division
        #   evaluate and sub into array
        # for all addition
        #   evaluate and sub into array
        
        print()
        
