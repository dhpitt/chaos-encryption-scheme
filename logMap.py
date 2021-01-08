# David Pitt
# Jan 5, 2021
# Implementation of the logistic map equation
# Brief demonstration of chaotic outputs

import numpy as np
import matplotlib.pylab as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as anim

def logisticEq(r,x0,steps):
    # The logistic equation is an iterative function
    # intended to model population growth with growth rate
    # r and initial population X0. At every step, the equation
    # is Xn+1 = rXn(1-Xn). X represents the ratio of the existing population
    # to the hypothetical carrying capacity (maximum possible pop).

    output = []
    x = x0
    for i in range(steps):
        output.append(x)
        x = r*x*(1-x)

    return output


def getLogisticValue():
    # A helper that will eventually return the value
    # at step n given r, x0 and n.
    return 0

# For values of r >= 3.56995, we see aperiodic oscillation.
# Slight changes in the initial conditions can cause
# big changes in the output. 
# At r > 4, we see negative population sizes.

# Analytics
def logisticEqWithCollisions(r,x0,steps,places):
    # Performs logistic equation and tests for collisions.
    collisions = 0
    output = []
    x = x0
    for i in range(steps):
        rounded = round(x,places)
        if rounded in output:
            collisions += 1
        output.append(rounded)
        x = r*x*(1-x)
    return collisions

def collisionChecker(steps,places):
    collisions = []
    for i in range(30):
        collisions.append(logisticEqWithCollisions(3.7,0.01*(i+1),steps,places))

    return collisions

def logisticEqWithRounding(r,x0,steps,places):
    # Performs logistic equation and rounds all values to
    # a number of decimal places.
    output = []
    x = x0
    for i in range(steps):
        output.append(round(x,places))
        x = r*x*(1-x)
    return output