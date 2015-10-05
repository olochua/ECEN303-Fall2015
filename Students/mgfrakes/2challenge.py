__author__ = "Morgan Frakes"
__NetID__ = "mgfrakes13"
__GitHubID__ = "mgfrakes"
__challenge__ = "2"
__version__ = "1.0"
__grader__ = ""
__SelfGrade__ = "5.0"
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


print "Part 1\n"

Trials = []
Pr4 = 0
for TrialIndex1 in range(0, NumberTrials):
    Trials.append(geometricflip(ParameterP))
    if Trials[TrialIndex1] == 4:
        Pr4 += 1.0

Solution1 = Pr4 / NumberTrials

print "The empirical probability that the  number of flips is 4 is " + repr(Solution1) + "."

EvenTrials = 0
for TrialIndex2 in range(0, NumberTrials):
    if Trials[TrialIndex2] % 2 == 0:
        EvenTrials += 1.0
PrE = EvenTrials / NumberTrials
Solution2 = Solution1 / PrE

print "The empirical probability that the number of flips is 4 conditional on number of flips being even is " \
      + repr(Solution2) + "."

print "\nPart 2\n"

Trials2 = []
Pr2 = PrA = PrB = 0
for TrialIndex2 in range(0, NumberTrials):
    FinalA = FinalB = Flips = 0
    while FinalA == FinalB:
        FinalA = biasedcoinflip(ParameterA)
        FinalB = biasedcoinflip(ParameterB)
        Flips += 1
    Trials2.append(Flips)
    if Trials2[TrialIndex2] == 2:
        Pr2 += 1.0
    if FinalA == 1:
        PrA += 1.0
    if FinalB == 1:
        PrB += 1.0

Solution3 = Pr2 / NumberTrials
Solution4 = PrA / NumberTrials
Solution5 = PrB / NumberTrials

print "The empirical probability that the number of flips is 2 is " + repr(Solution3) + "."

print "The empirical probability that coin A is showing 1 when the stopping condition is met is " \
      + repr(Solution4) + "."

print "The empirical probability that coin B is showing 1 when the stopping condition is met is " \
      + repr(Solution5) + "."