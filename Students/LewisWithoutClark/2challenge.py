__author__ = "Justin Lewis"
__NetID__ = "justin94lewis"
__GitHubID__ = "LewisWithoutClark"
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


ParameterP = 1.0/3.0    # Parameter of digital coin
ParameterA = 1.0/3.0    # Parameter of digital coin A
ParameterB = 1.0/2.0    # Parameter of digital coin B
NumberTrials = 100000

def biasedcoinflip(p=0.5):

    return int( math.floor(random.random() + p))


def geometricflip(p=0.5):

    numberflips = 1
    while biasedcoinflip(p) != 1:
        numberflips += 1
    return numberflips

def geometricflip2(pA=0.5,pB=0.5):
    a=0
    b=0

    numberflips = 0
    while (a^b) != 1:
        a = biasedcoinflip(pA)
        b = biasedcoinflip(pB)
        numberflips += 1
    return numberflips

def geometricflipCond(pA=0.5,pB=0.5,aVal=0,bVal=0):
    a=0
    b=0

    while (a^b) != 1:
        a = biasedcoinflip(pA)
        b = biasedcoinflip(pB)

    if (a == aVal) & (b == bVal):
        return 1
    else:
        return 0

print "Part 1\n"

Trials = []
for TrialIndex1 in range(0, NumberTrials):
    Trials.append(geometricflip(ParameterP))

Solution1 = Trials.count(4) / (1.0*NumberTrials)

print "The empirical probability that the  number of flips is 4 is " \
      + str(Solution1) + "."

EvenTrials = 0

for TrialIndex2 in range(0, NumberTrials):
    if (Trials[TrialIndex2] % 2) == 0:
        EvenTrials += 1

Solution2 = (Solution1 * 1.0*NumberTrials) / (1.0*EvenTrials)

print "The empirical probability that the number of flips is 4 conditional on number of flips being even is " \
    + str(Solution2) + "."


print "\nPart 2\n"

Trials2 = []

for TrialIndex3 in range(0, NumberTrials):
    Trials2.append(geometricflip2(ParameterA,ParameterB))

Solution3 = Trials2.count(2) / (1.0*len(Trials2))

print "The empirical probability that the number of flips is 2 is " \
    + str(Solution3) + "."

Trials3 = []
for TrialIndex4 in range(0, NumberTrials):
    Trials3.append(geometricflipCond(ParameterA,ParameterB,1,0))

Solution4 = Trials3.count(1) / (1.0*len(Trials3))

print "The empirical probability that coin A is showing 1 when the stopping condition is met is " \
    + str(Solution4) + "."

Trials4 = []
for TrialIndex4 in range(0, NumberTrials):
    Trials4.append(geometricflipCond(ParameterA,ParameterB,0,1))

Solution5 = Trials4.count(1) / (1.0*len(Trials4))

print "The empirical probability that coin B is showing 1 when the stopping condition is met is " \
    + str(Solution5) + "."
