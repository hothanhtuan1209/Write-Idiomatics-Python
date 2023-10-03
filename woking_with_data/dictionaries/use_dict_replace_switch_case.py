"""
- Use a dict as a substitute for a switch...case statement.
- Functions are treated as values and stored in dictionaries, allowing for clear, efficient dispatch based on keys, such as mapping operators in a calculator.
- This approach can be applied to various scenarios, showcasing Python's flexibility and the power of treating everything as an object.
"""

import operator as op

# Harmful solution
# def apply_operation(left_operand, right_operand, operator):
#     if operator == "+":
#         return left_operand + right_operand

#     elif operator == "-":
#         return left_operand - right_operand

#     elif operator == "*":
#         return left_operand * right_operand

#     elif operator == "/":
#         return left_operand / right_operand


# Idiomatic solution
def apply_operation(left_operand, right_operand, operator):
    """
    Apply a mathematical operation to two operands.

    Args:
        left_operand (float): The left operand.
        right_operand (float): The right operand.
        operator (str): The operator symbol ('+', '-', '*', '/').

    Returns:
        float: The result of the operation.
    """

    operator_mapper = {"+": op.add, "-": op.sub, "*": op.mul, "/": op.truediv}

    return operator_mapper[operator](left_operand, right_operand)
