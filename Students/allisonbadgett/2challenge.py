__author__ = "Allison Badgett"
__NetID__ = "allisonbadgett"
__GitHubID__ = "allisonbadgett"
__challenge__ = "2"
__version__ = "0.0"
__grader__ = ""
__SelfGrade__ = "5"
__PeerGrade__ = ""

"""
Random Signals and Systems
Course: ECEN 303-502
Maximum Grade: 5pt
"""

import random
import math
import matplotlib.pyplot as plt


ParameterP = 1.0/3.0    # Parameter of digital coin
ParameterA = 1.0/3.0    # Parameter of digital coin A
ParameterB = 1.0/2.0    # Parameter of digital coin B
NumberTrials = 100000


def biasedcoinflip(p=0.5):
    """
    This method returns a one with probability p and it returns a zero with
    probability (1 - p). The default parameter is p=0.5; this can be changed
    by passing an argument to the method.
    """
    return math.floor(random.random() + p)


def geometricflip(p=0.5):
    """
    This method returns a natural number that denotes the number of digital
    coin flips needed to obtain a one. It relies on method biasedcoinflip().
    """
    numberflips = 1
    while biasedcoinflip(p) != 1:
        numberflips += 1
    return numberflips


print("Part 1\n") #altered to work with Python 3.4

numFour =0
Trials = []
for TrialIndex1 in range(0, NumberTrials):
    Trials.append(geometricflip(ParameterP))
    if Trials[TrialIndex1] == 4:
        numFour += 1    #increments if number of flips is 4

print("The empirical probability that the  number of flips is 4 is " + repr(numFour/NumberTrials) + ".") #altered to work with Python 3.4

EvenTrials = 0
for TrialIndex2 in range(0, NumberTrials):
    if Trials[TrialIndex2] % 2 == 0:
        EvenTrials += 1 #increments if number of flips is even

print("The empirical probability that the number of flips is 4 conditional on number of flips being even is "+ repr(numFour/EvenTrials) + ".") #altered to work with Python 3.4


print("\nPart 2\n") #altered to work with Python 3.4

Trials2 = []
FinalA = 0
FinalB = 0
numTwo =0

for TrialIndex2 in range(0, NumberTrials):
    coinA = geometricflip(ParameterA)
    coinB = geometricflip(ParameterB)
    if coinA > coinB:   #if B is the stopping condition
        Trials2.append(coinB)
        FinalB += 1
    elif coinA < coinB: #if A is the stopping condition
        Trials2.append(coinA)
        FinalA += 1
    else:       #if both coins are stopping condition
        Trials2.append(coinA)
        FinalA += 1
        FinalB += 1

for TrialIndex2 in range(0, NumberTrials):  #find number of times number of flips is 2
    if Trials2[TrialIndex2] == 2:
        numTwo += 1

print("The empirical probability that the number of flips is 2 is "+ repr(numTwo/NumberTrials) + ".") #altered to work with Python 3.4
print("The empirical probability that coin A is showing 1 when the stopping condition is met is "+ repr(FinalA/NumberTrials) +".") #altered to work with Python 3.4
print("The empirical probability that coin B is showing 1 when the stopping condition is met is "+ repr(FinalB/NumberTrials)  + ".") #altered to work with Python 3.4
