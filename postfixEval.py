# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 15:27:02 2020

@author: stdon
"""

from pythonds.basic import Stack

def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token,operand1,operand2)
            operandStack.push(result)
    return operandStack.pop()

def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    elif op == "-":
        return op1 - op2
    else:
        op = input('Error: ' + op +' is not a recognized operator \nPlease enter an alternative operator: ')
        return doMath(op, op1, op2)

print(postfixEval('10 3 5 * 16 4 - / +'))
