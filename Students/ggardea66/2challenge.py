__author__ = "Gissel Gardea"
__NetID__ = "gardegi059"
__GitHubID__ = "ggardea66"
__challenge__ = "2"
__version__ = "3.5.0"
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
TrialSequence=[]

def biasedcoinflip(p=0.5):
    for TrialIndex in range(0,NumberTrials):
        TrialSequence.append(random.randrange(2))
        if (sum(TrialSequence)/(1.0*len(TrialSequence))) < ParameterP:
            TrialSequence[len(TrialSequence)-1]=1
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


print "Part 1\n"

Trials = []
for TrialIndex1 in range(0, NumberTrials):
    Trials.append(geometricflip(ParameterP))

TrialFour = ((1.0*Trials.count(4))/(1.0*len(Trials)))

print ("The empirical probability that the  number of flips is 4 is {0:.4f}." .format(TrialFour))
print(repr(Trials))

ProbEven = []
for TrialIndex2 in range(0, NumberTrials):
    Evenfilter = []
    Evenfilter.append(geometricflip(ParameterP))
    if Evenfilter[0]%2 == 0:
        ProbEven.append(Evenfilter[0])
ProbIsEven= ((1.0*ProbEven.count(4)))/ (1.0*len(ProbEven))

print "The empirical probability that the number of flips is 4 conditional on number of flips being even is {0:.4f}." .format(ProbIsEven)
print(repr(ProbEven))

print "\nPart 2\n"

CountOfFlips = []
Heads = []
for TrialIndex2 in range(0,NumberTrials):
    FinalA = 0
    FinalB = 0
    Win = 0
    count = 0
    while Win == 0:
        FinalA = biasedcoinflip(ParameterP)
        FinalB = biasedcoinflip(ParameterP)
        if (1.0*FinalA +1.0*FinalB) == 1.0:
            Win = 1
            count += 1
            CountOfFlips.append(count)
            Heads.append(FinalA)
        else:
            count += 1
            Win = 0

TwoProb = ((1.0*CountOfFlips.count(2))/(1.0*len(CountOfFlips)))
ProbA = ((1.0*Heads.count(1))/(1.0*len(Heads)))
ProbB = ((1.0*Heads.count(0)))/ (1.0*len(Heads))

print "The empirical probability that the number of flips is 2 is {0:.4f}." .format(TwoProb)
print(repr(CountOfFlips))

print "The empirical probability that coin A is showing 1 when the stopping condition is met is {0:.4f}." .format(ProbA)
print(repr(Heads))
print "The empirical probability that coin B is showing 1 when the stopping condition is met is {0:.4f}." .format(ProbB)
print(repr(Heads))


