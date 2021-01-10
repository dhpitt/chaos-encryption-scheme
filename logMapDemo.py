# David Pitt
# Jan 5, 2021
# Implementation of the logistic map equation
# Brief demonstration of chaotic outputs

import numpy as np
import matplotlib.pylab as plt

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

chaoticLimit = 3.56995
numSteps = 100

t = list(range(numSteps))
    
# Plot the output

fig = plt.figure()
ax = plt.subplot(224)
ax.set(xlim=(0,t[-1]),ylim=(0,1))

normalGrowth = plt.subplot(221)
normalGrowth.set(xlim=(0,t[-1]),ylim=(0,1))

normalDecay = plt.subplot(222)
normalDecay.set(xlim=(0,t[-1]),ylim=(0,1))

chaos1 = plt.subplot(223)
chaos1.set(xlim=(0,t[-1]),ylim=(0,1))

plt.style.use('seaborn-pastel')

plt.xlabel('[t] = nt')
plt.ylabel('X(t)')
plt.title('Chaotic Logistic Map')

for i in range(4):
    ax.plot(t,logisticEq(3.7,0.005*i,numSteps),label="x0 = {}".format(0.05*i))
chaos1.plot(t,logisticEq(3.7,0.1,numSteps))

normalGrowth.plot(t,logisticEq(1.8,0.1,numSteps))
normalDecay.plot(t,logisticEq(0.8,0.8,numSteps))
ax.legend()
plt.show()

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

#logisticEqWithCollisions(3.7,0.3,255,6)

def collisionChecker(steps,places):
    collisions = 0
    for i in range(2000):
        collisions += logisticEqWithCollisions(3.7,0.0005*(i+1),steps,places)
    return collisions

print(collisionChecker(255,7))
#print(collisionChecker(26,4))

def logisticEqWithRounding(r,x0,steps,places):
    # Performs logistic equation and rounds all values to
    # a number of decimal places.
    output = []
    x = x0
    for i in range(steps):
        output.append(round(x,places))
        x = r*x*(1-x)
    return output