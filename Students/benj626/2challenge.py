__author__ = "Benjamin Johnston"
__NetID__ = "415004772"
__GitHubID__ = "benj626"
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
#import matplotlib.pyplot as plt

#Print statements were modified to work with Python 3.4

ParameterP = 1.0/3.0    # Parameter of digital coin
ParameterA = 1.0/3.0    # Parameter of digital coin A
ParameterB = 1.0/2.0    # Parameter of digital coin B
NumberTrials = 100000
four_flips = 0
two_flips = 0

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

print ("Part 1\n")


Trials = []
for TrialIndex1 in range(0, NumberTrials):
    Trials.append(geometricflip(ParameterP))
    if Trials[TrialIndex1] == 4:
        four_flips += 1

print ("The empirical probability that the  number of flips is 4 is " \
       + repr(four_flips/NumberTrials) \
       + ".")

EvenTrials = 0
for TrialIndex2 in range(0, NumberTrials):
    if Trials[TrialIndex2] % 2 == 0:
        EvenTrials += 1

print ("The empirical probability that the number of flips is 4 conditional on number of flips being even is " \
    + repr(four_flips/EvenTrials) \
    + ".")


print ("\nPart 2\n")

Trials2 = []
FinalA = 0
FinalB = 0

for TrialIndex2 in range(0, NumberTrials):
    coin_A = geometricflip(ParameterA)
    coin_B = geometricflip(ParameterB)
    if coin_A < coin_B:   #stops on A
        Trials2.append(coin_A)
        FinalA += 1

    elif coin_A > coin_B:     #stops on B
        Trials2.append(coin_B)
        FinalB += 1

    else: #If they equal one another
        Trials2.append(coin_A)
        FinalA += 1
        FinalB += 1

for TrialIndex2 in range(0, NumberTrials):
    if Trials2[TrialIndex2] == 2:
        two_flips += 1

print ("The empirical probability that the number of flips is 2 is " \
    + repr(two_flips/NumberTrials) \
    + ".")
print ("The empirical probability that coin A is showing 1 when the stopping condition is met is " \
    + repr(FinalA/NumberTrials) \
    + ".")
print ("The empirical probability that coin B is showing 1 when the stopping condition is met is " \
    + repr(FinalB/NumberTrials) \
    + ".")
