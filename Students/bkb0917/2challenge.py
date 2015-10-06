__author__ = "Bailey Barksdale"
__NetID__ = "bailey13"
__GitHubID__ = "bkb0917"
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
import matplotlib.pyplot


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
Solution1 = 0
for TrialIndex1 in range(0, NumberTrials):
    Trials.append(geometricflip(ParameterP))

for TrialIndex2 in range(0, NumberTrials):
    if Trials[TrialIndex2]==4:
           Solution1 +=1

Solution1 /= NumberTrials

print("The empirical probability that the  number of flips is 4 is "  + repr(Solution1) + ".")

EvenTrials = 0
NumEven = 0
for TrialIndex3 in range(0, NumberTrials):
    if Trials[TrialIndex3]%2==0:
        NumEven += 1
        if Trials[TrialIndex3]==4:
           EvenTrials += 1

EvenTrials /= NumEven


print("The empirical probability that the number of flips is 4 conditional on number of flips being even is " + repr(EvenTrials)
    + ".")


print("\nPart 2\n")

Trials2 = []
FinalA = 0
FinalB = 0
Aflips = 0
Bflips = 0
CoinResults = []
for TrialIndex4 in range(0, NumberTrials):
    Aflips = geometricflip(ParameterA)
    Bflips = geometricflip(ParameterB)
    if Aflips<Bflips:
        Trials2.append(Aflips)
        CoinResults.append(0)
    elif Aflips>Bflips:
        Trials2.append(Bflips)
        CoinResults.append(1)
    else:
        Trials2.append(Aflips)
        CoinResults.append(2)


Solution3 = 0
for TrialIndex5 in range(0, NumberTrials):
    if Trials2[TrialIndex5]==2:
        Solution3 += 1

Solution3 /= NumberTrials
AOnes = 0
BOnes = 0
for TrialIndex6 in range(0, NumberTrials):
    if CoinResults[TrialIndex6]==0:
        AOnes += 1
    elif CoinResults[TrialIndex6]==1:
        BOnes += 1
    else:
        AOnes += 1
        BOnes += 1

AOnes /= NumberTrials
BOnes /= NumberTrials


print("The empirical probability that the number of flips is 2 is "  + repr(Solution3)+ ".")
print("The empirical probability that coin A is showing 1 when the stopping condition is met is " + repr(AOnes)
    + ".")
print("The empirical probability that coin B is showing 1 when the stopping condition is met is " + repr(BOnes)
    + ".")

