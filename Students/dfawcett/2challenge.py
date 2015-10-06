__author__ = "David Fawcett"
__NetID__ = "dgf378"
__GitHubID__ = "dfawcett"
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


print("Part 1\n")

Trials = []
for TrialIndex1 in range(0, NumberTrials):
    Trials.append(geometricflip(ParameterP))

probability4 = Trials.count(4)/NumberTrials

print("The empirical probability that the  number of flips is 4 is " \
    # EDIT: + repr(Solution1)) \
    + repr(probability4) + ".")

EvenTrials = 0
for TrialIndex2 in range(0, NumberTrials):
    #
    # EDIT
    #
    if Trials[TrialIndex2] % 2 == 0:
        EvenTrials += 1

probabilityeven = Trials.count(4)/EvenTrials;

print("The empirical probability that the number of flips is 4 conditional on number of flips being even is " \
    # EDIT: + repr(Solution2)) \
    + repr(probabilityeven) + ".")


print("\nPart 2\n")

Trials2 = []
Trials3 = []
FinalA = 0
FinalB = 0
for TrialIndex2 in range(0, NumberTrials):
    #
    # EDIT
    #
    NumFlips = 0
    FinalA = 0
    FinalB = 0
    while(FinalA == FinalB):
        FinalA = biasedcoinflip(ParameterA)
        FinalB = biasedcoinflip(ParameterB)
        NumFlips += 1
    Trials2.append(NumFlips)
    if(FinalA == 1):
        Trials2.append('A')
    else:
        Trials2.append('B')


print("The empirical probability that the number of flips is 2 is " \
    # EDIT: + repr(Solution3)) \
    + repr(Trials2.count(2)/NumberTrials) + ".")
print("The empirical probability that coin A is showing 1 when the stopping condition is met is " \
    # EDIT: + repr(Solution4)) \
    + repr(Trials2.count('A')/NumberTrials) + ".")
print("The empirical probability that coin B is showing 1 when the stopping condition is met is " \
    # EDIT: + repr(Solution5)) \
    + repr(Trials2.count('B')/NumberTrials) + ".")


