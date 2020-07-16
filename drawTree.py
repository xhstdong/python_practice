# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 11:40:40 2020

@author: stdon
"""

import turtle
import random

def tree(branchLen,t):
    if branchLen > 5:
        right_angle = random.randrange(15, 45)
        left_angle = random.randrange(30, 90)
        length_factor = random.uniform(0.5, 1)
        t.pensize(branchLen/75)
        t.pencolor((branchLen/255, 1.0-branchLen/255, branchLen/255))
        t.forward(length_factor * branchLen)
        t.right(right_angle)
        tree(branchLen-15,t)
        t.left(left_angle)
        tree(branchLen-15,t)
        t.right(left_angle - right_angle)
        t.backward(length_factor * branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75,t)
    myWin.exitonclick()

main()