# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 15:13:44 2020

@author: stdon
"""

from pythonds.basic import Stack

def infixToPostfix(infixexpr):
    prec = {}
    my_operators=["+","-","/","*","**"]
    prec["**"]= 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            try:
                greater_prec = prec[opStack.peek()] >= prec[token])
            except:
                print('Warning: ' + token ' is not a recognized operator')
                token=input('please enter another operator: ')
                while token not in my_operators:
                    token = input('sorry that is not a reocgnized operator. Please enter another operator: ')
                greater_prec = prec[opStack.peek()] >= prec[token])
            while (not opStack.isEmpty()) and \
               greater_prec:
                  postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)

print(infixToPostfix("5 * 3 ** ( 4 - 2 )"))
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))
