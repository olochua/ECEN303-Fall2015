__author__ = "Shannon Morrissey"
__NetID__ = "shannon.morrissey"
__GitHubID__ = "shmorrissey"
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


print ("Part 1\n")

Trials = []
Prob4 = 0
for TrialIndex1 in range(0, NumberTrials):
    Trials.append(geometricflip(ParameterP))
    if Trials[TrialIndex1] == 4:
        Prob4 += 1.0

Solution1 = Prob4 / NumberTrials

print ("The empirical probability that the  number of flips is 4 is " + repr(Solution1) + ".")
#count for even trials
EvenTrials = 0
for TrialIndex2 in range(0, NumberTrials):
    if Trials[TrialIndex2] % 2 == 0:
        EvenTrials += 1.0
PrEv = EvenTrials / NumberTrials
Solution2 = Solution1 / PrEv

print ("The empirical probability that the number of flips is 4 conditional on number of flips being even is " \
      + repr(Solution2) + ".")

print ("\nPart 2\n")

Trials2 = []
Prob2 = ProbA = ProbB = 0
for TrialIndex2 in range(0, NumberTrials):
    FinalA = FinalB = Flips = 0
    while FinalA == FinalB:
        FinalA = biasedcoinflip(ParameterA)
        FinalB = biasedcoinflip(ParameterB)
        Flips += 1
    Trials2.append(Flips)
    if Trials2[TrialIndex2] == 2:
        Prob2 += 1.0
    if FinalA == 1:
        ProbA += 1.0
    if FinalB == 1:
        ProbB += 1.0

Solution3 = Prob2 / NumberTrials
Solution4 = ProbA / NumberTrials
Solution5 = ProbB / NumberTrials

print ("The empirical probability that the number of flips is 2 is " + repr(Solution3) + ".")

print ("The empirical probability that coin A is showing 1 when the stopping condition is met is " \
      + repr(Solution4) + ".")

print ("The empirical probability that coin B is showing 1 when the stopping condition is met is " \
      + repr(Solution5) + ".")
