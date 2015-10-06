__author__ = "Stephanie Demco"
__NetID__ = "steph1995"
__GitHubID__ = "stephaniedemco"
__challenge__ = "2"
__version__ = "0.0"
__grader__ = ""
__SelfGrade__ = ""
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
probFour = 0
for TrialIndex1 in range(0, NumberTrials):
    Trials.append(geometricflip(ParameterP))
    if Trials[TrialIndex1] == 4:
        probFour += 1

Solution1 = probFour/NumberTrials

print "The empirical probability that the  number of flips is 4 is "+ repr(Solution1) + "."

EvenTrials = 0
for TrialIndex2 in range(0, NumberTrials):
    if Trials[TrialIndex2]%2 == 0:
        EvenTrials += 1.0
Even = EvenTrials / NumberTrials
Solution2 = Solution1 / Even


print "The empirical probability that the number of flips is 4 conditional on number of flips being even is "  + repr(Solution2)+ "."


print "\nPart 2\n"

Trials2 = []
prob2 = 0
probB = 0
probA = 0

for TrialIndex2 in range(0, NumberTrials):
    FinalA = 0
    FinalB = 0
    Flips = 0
    while FinalA == FinalB:
        FinalA = biasedcoinflip(ParameterA)
        FinalB = biasedcoinflip(ParameterB)
        Flips += 1
    Trials2.append(Flips)
    if Trials2[TrialIndex2] == 2:
        prob2 += 1
    if FinalA == 1:
        probA += 1
    if FinalB == 1:
        probB += 1

Solution3 = prob2/NumberTrials
Solution4 = probA/NumberTrials
Solution5 = probB/NumberTrials

print "The empirical probability that the number of flips is 2 is " + repr(Solution3) + "."
print "The empirical probability that coin A is showing 1 when the stopping condition is met is " + repr(Solution4)+ "."
print "The empirical probability that coin B is showing 1 when the stopping condition is met is " + repr(Solution5) + "."




print "The empirical probability that the number of flips is 2 is " + repr(Solution3) + "."

print "The empirical probability that coin A is showing 1 when the stopping condition is met is " \
      + repr(Solution4) + "."

print "The empirical probability that coin B is showing 1 when the stopping condition is met is " \
      + repr(Solution5) + "."
