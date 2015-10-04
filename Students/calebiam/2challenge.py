__author__ = "Caleb Holley"
__NetID__ = "calebiam"
__GitHubID__ = "calebiam"
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
NumberTrials = 1000
TrialSequence = []


def biasedcoinflip(p=0.5):
    for TrialIndex in range(0, NumberTrials):
        TrialSequence.append(random.randrange(2))
        if (sum(TrialSequence)/ (1.0 *len(TrialSequence))) < ParameterP:
            TrialSequence[len(TrialSequence)-1] = 1
            return 1
        else:
            TrialSequence[len(TrialSequence)-1] = 0
            return 0
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



print("Part 1\n")   #changed many print statements throughout to work with updated python version

Trials = []

for TrialIndex1 in range(0, NumberTrials):
    Trials.append(geometricflip(ParameterP))

probfour = ((1.0*Trials.count(4))/ (1.0*len(Trials)))

print( "The empirical probability that the  number of flips is 4 is {0:.4f}.".format(probfour))
print(repr(Trials))


EvenTrials = []
for TrialIndex2 in range(0, NumberTrials):
    Evenfilter = []
    Evenfilter.append(geometricflip(ParameterP))
    if Evenfilter[0]%2 == 0:
        EvenTrials.append(Evenfilter[0])
probgiveneven = ((1.0*EvenTrials.count(4))/ (1.0*len(EvenTrials)))


print( "The empirical probability that the number of flips is 4 conditional on number of flips being even is {0:.4f}.".format(probgiveneven))
print(repr(EvenTrials))

print( "\nPart 2\n")

Flipscount = []
Aheadsup = []
for TrialIndex2 in range(0, NumberTrials):
    FinalA = 0
    FinalB = 0
    Success = 0
    count = 0
    while Success == 0:
        FinalA = biasedcoinflip(ParameterP)
        FinalB = biasedcoinflip(ParameterP)
        if (1.0*FinalA + 1.0*FinalB) == 1.0:
            Success = 1
            count += 1
            Flipscount.append(count)
            Aheadsup.append(FinalA)
        else:
            count += 1
            Success = 0

probtwo = ((1.0*Flipscount.count(2))/ (1.0*len(Flipscount)))
probA = ((1.0*Aheadsup.count(1))/ (1.0*len(Aheadsup)))
probB = ((1.0*Aheadsup.count(0))/ (1.0*len(Aheadsup)))

print( "The empirical probability that the number of flips is 2 is {0:.4f}.".format(probtwo))
print(repr(Flipscount))

print( "The empirical probability that coin A is showing 1 when the stopping condition is met is {0:.4f}.".format(probA))
print(repr(Aheadsup))

print("The empirical probability that coin B is showing 1 when the stopping condition is met is {0:.4f}.".format(probB))
print(repr(Aheadsup))
