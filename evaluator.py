from enum import Enum

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

class ExpressionTreeNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right
        
        self.is_number = True
        self.number = 0.0
        self.operator = OperatorType.ADDITION

    def set_number(self, number):
        self.number = number

    def set_operator(self, operator):
        self.operator = operator

class Evaluator():
    def __init__(self, array_expression):
        self.array_expression = array_expression

    def parse_array(self):
        print()
        # get index of operator with highest prio and create node
        # check if left and right in array are numbers or expressions
        # if number, set node children accordingly
        # else 
        #   

        # For each bracket in array
        #   use tokenizer to parse into array
        #   recursively parse output array to get root node of bracket
        #   get operator to left and right of bracket index, compare

        # linear search for operator of highest prio
        # create node with operator, set left and right accordingly
        # if left or right is expression    
        #   create node with bracket, operator of highest prio, and other number
        
