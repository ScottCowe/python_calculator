from structures import *

class Operator:
    def __init__(self, as_str):
        self.as_str = as_str
        self.prec = Operator.precedence(self.as_str)

        if not Operator.isOperator(self.as_str):
            raise Exception(f"'{self.as_str}' is not an operator")

    @staticmethod
    def precedence(operator):
        match operator:
            case "+":
                return 1
            case "-":
                return 1
            case "*":
                return 2
            case "/":
                return 2
            case "^":
                return 3
            case _:
                return 0 # not an operator

    @staticmethod
    def isOperator(operator):
        return Operator.precedence(operator) != 0

class Expression:
    def __init__(self):
        self.type = 0 # 0 for postfix, 1 for infix
        self.expr = ""

    def from_postfix(self, postfix):
        self.expr = postfix
        self.type = 0

        return self

    # infix should be an expression with each token seperated by a space
    def from_infix(self, infix):
        self.type = 1

        tokens = infix.split(" ")

        stack = Stack()
        postfix = ""

        for i in tokens:
            isOperator = Operator.precedence(i) != 0

            if isOperator:
                op_prec = Operator.precedence(i)

                while not stack.isEmpty() and stack.peek() != "(" and (Operator.precedence(stack.peek()) > op_prec or (op_prec == Operator.precedence(stack.peek()) and i != "^")):
                    postfix += stack.pop() + " "

                stack.push(i)
            elif i == "(":
                stack.push(i)
            elif i == ")":
                while stack.peek() != "(":
                    postfix += stack.pop() + " "

                if stack.isEmpty():
                    raise Exception("Unmatched brackets")

                stack.pop() # discard '('
            else: # token is a number
                postfix += i + " "

        while not stack.isEmpty():
            postfix += stack.pop() + " "

        self.expr = postfix

        return self

class ExpressionTreeNode:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

class ExpressionTree:
    def __init__(self):
        self.root_node = None

    @staticmethod
    def from_postfix(postfix):
        print()

    @staticmethod
    def evaluate(expression_tree):
        return 0
