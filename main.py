from expression import *

expression = Expression().from_infix("3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3")
print(expression.expr)
