__author__ = "Alejandro Penaloza Rodriguez"
__NetID__ = "alex23"
__GitHubID__ = "alex23tamu"
__challenge__ = "2"
__version__ = "0.0"
__grader__ = ""
__SelfGrade__ = "3"
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
TrialSeq = []


def biasedcoinflip(p=0.5):

#Part 1

    for TrialIndex in range(0, NumberTrials):
    TrialSeq.append(random.randrange(2))
    if (sum(TrialSeq) / (1.0 * len(TrialSeq))) < ParameterP:
    TrialSeq[len(TrialSeq) - 1] = 1
    return 1
    else:
    TrialSeq[len(TrialSeq) - 1] = 0
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

# Part 2

prfour = ((1.0*Trials.count(4)) / (1.0*len(Trials)))

print "The empirical probability that the  number of flips is 4 is {0:.4f}.".format(prfour)

print repr(Trials)

EvenTrials = []
for TrialIndex2 in range(0, NumberTrials):
 Evenmatch = []
 Evenmatch.append(geometricflip(ParameterP))
 if Evenmatch[0]%2 == 0:
 EvenTrials.append(Evenmatch[0])
 preven = ((1.0*EvenTrials.count(4)) / (1.0*len(EvenTrials)))




print "The empirical probability that the number of flips is 4 conditional on number of flips being even is {0:.4f}.".format(preven)

print repr(EvenTrials)

print "\nPart 2\n"

Trials2 = []
Heads = []
FinalA = 0
FinalB = 0
for TrialIndex2 in range(0, NumberTrials):

     FinalA = 0
     FinalB = 0
     count = 0
     Correct = 0

        while Correct == 0:

        FinalA = biasedcoinflip(ParameterP)
        FinalB = biasedcoinflip(ParameterP)

      if (1.0*FinalA + 1.0*FinalB) == 1.0:

      Correct = 1
      count += 1
      Trials2.append(count)
      Heads.append(FinalA)

      else:

      count += 1
      Correct = 0

     prtwo = ((1.0*Trials2.count(2)) / (1.0*len(Trials2)))
     prA = ((1.0*Heads.count(1)) / (1.0*len(Heads)))
     prB = ((1.0*Heads.count(0)) / (1.0*len(Heads)))



print "The empirical probability that the number of flips is 2 is {0:.4f}.".format(prtwo)
print repr(Trials2)

print "The empirical probability that coin A is showing 1 when the stopping condition is met is {0:.4f}.".format(prA)
print repr(Heads)

print "The empirical probability that coin B is showing 1 when the stopping condition is met is {0:.4f}.".format(prB)
print repr(Heads)

