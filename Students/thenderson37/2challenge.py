__author__ = "Tyler Henderson"
__NetID__ = "tyler.henderson07"
__GitHubID__ = "thenderson37"
__challenge__ = "2"
__version__ = "3.4"
__grader__ = ""
__SelfGrade__ = "4"
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
NumberTrials = 10000      #I changed the number of trials because it was displaying wrong with 100000

TrialSequence = []

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



print("Part 1\n")   #added () to work with version 3.4

Trials = []

for TrialIndex1 in range(0, NumberTrials):
    Trials.append(geometricflip(ParameterP))

probability_four = (Trials.count(4))/(len(Trials))

print("The empirical probability that the  number of flips is 4 is {0:.4f}.".format(probability_four))
print(repr(Trials))


EvenTrials = []

for TrialIndex2 in range(0, NumberTrials):

    Evens = []
    Evens.append(geometricflip(ParameterP))

    if Evens[0]%2 == 0: #if divisible by 2 then store in Evens

        EvenTrials.append(Evens[0])

probability_even = (EvenTrials.count(4))/ (len(EvenTrials)) #count the number of 4s in Evens and divide by total


print("The empirical probability that the number of flips is 4 conditional on number of flips being even is {0:.4f}.".format(probability_even))
print(repr(EvenTrials))

print( "\nPart 2\n")

Flips = []
Heads = []
FinalA = 0
FinalB = 0

for TrialIndex2 in range(0, NumberTrials):

    S = 0
    count = 0

    while S == 0:

        FinalA = biasedcoinflip(ParameterP)
        FinalB = biasedcoinflip(ParameterP)

        if (FinalA + FinalB) == 1.0:

            S = 1
            count = count + 1
            Flips.append(count)
            Heads.append(FinalA)

        else:

            count = count + 1
            S = 0

probability_two = (Flips.count(2))/ (len(Flips))

CoinA = (Heads.count(1))/ (len(Heads))

CoinB = (Heads.count(0))/ (len(Heads))

print("The empirical probability that the number of flips is 2 is {0:.4f}.".format(probability_two))
print(repr(Flips))

print("The empirical probability that coin A is showing 1 when the stopping condition is met is {0:.4f}.".format(CoinA))
print(repr(Heads))

print("The empirical probability that coin B is showing 1 when the stopping condition is met is {0:.4f}.".format(CoinB))
print(repr(Heads))

