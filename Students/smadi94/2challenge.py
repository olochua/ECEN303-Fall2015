__author__ = "Zachary Smadi"
__NetID__ = "smadi94"
__GitHubID__ = "smadi94"
__challenge__ = "2"
__version__ = "3.5"
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
NumberTrials = 100000


def biasedcoinflip(p=0.5):
    if random.random() <= p:
        return 1
    else:
        return 0

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
PrFour = Trials.count(4)/float(NumberTrials)

print ("The empirical probability that the  number of flips is 4 is " + repr(PrFour) + ".")

EvenTrials = 0
for TrialIndex2 in range(0, NumberTrials):
    if Trials[TrialIndex2]%2 == 0:  # The Trials is multiple of 2
        EvenTrials +=1
        PrEven = Trials.count(4)/float(EvenTrials)

print ("The empirical probability that the number of flips is 4 conditional on number of flips being even is " + repr(PrEven) + ".")

print "\nPart 2\n"

Trials2 = []
Atrial = 0
Btrial = 0
for TrialIndex2 in range(0, NumberTrials):
    numFlips = 0
    Anow = 0
    Bnow = 0
    while Anow == Bnow:
        Anow = biasedcoinflip(ParameterA)
        Bnow = biasedcoinflip(ParameterB)
        numFlips += 1
    Trials2.append(numFlips)
    Atrial += Anow
    Btrial += Bnow
    if numFlips == 2:
        Trials2.append(1)

Prob1 = Trials2.count(2)/float(NumberTrials)
Prob2 = Atrial/ float(NumberTrials)
Prob3 = Btrial/ float(NumberTrials)

print ("The empirical probability that the number of flips is 2 is " + repr(Prob1) + ".")
print ("The empirical probability that coin A is showing 1 when the stopping condition is met is " + repr(Prob2) + ".")
print ("The empirical probability that coin B is showing 1 when the stopping condition is met is " + repr(Prob3) + ".")
