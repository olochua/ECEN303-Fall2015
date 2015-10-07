__author__ = "Weston Torti"
__NetID__ = "tort115"
__GitHubID__ = "westort"
__challenge__ = "2"
__version__ = "1.0"
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
    if random.random() <= p: #standard coin flip biasing
        return 1
    else:
        return 0

    return math.floor(random.random() + p)


def geometricflip(p=0.5):

    numberflips = 1
    while biasedcoinflip(p) != 1:
        numberflips += 1 #summing coin flips
    return numberflips


print "Part 1\n"

Trials = []
for TrialIndex1 in range(0, NumberTrials):

    Trials.append(geometricflip(ParameterP))
Solution1 = Trials.count(4)/float(NumberTrials)


print ("The empirical probability that the  number of flips is 4 is %f." % Solution1)
EvenTrials = 0
for TrialIndex2 in range(0, NumberTrials):
    A= geometricflip(ParameterP)
    if A % 2 == 0:
       EvenTrials += 1
Solution2 = Trials.count(4)/float(EvenTrials)
print ("The empirical probability that the number of flips is 4 conditional on number of flips being even is %f " % Solution2)


print "\nPart 2\n"

Trials2 = []
FinalA = 0
FinalB = 0
for TrialIndex2 in range(0, NumberTrials):
    numFlips = 0
    CurrentA = 0
    CurrentB = 0
    while CurrentA == CurrentB:
        CurrentA = biasedcoinflip(ParameterA)
        CurrentB = biasedcoinflip(ParameterB)
        numFlips += 1
    Trials2.append(numFlips)
    FinalA += CurrentA
    FinalB += CurrentB
    if numFlips == 2:
        Trials2.append(1)
Solution3 = Trials2.count(2)/float(NumberTrials)
Solution4 = FinalA/float(NumberTrials)
Solution5 = FinalB/float(NumberTrials)

print "The empirical probability that the number of flips is 2 is %f " % Solution3

print "The empirical probability that coin A is showing 1 when the stopping condition is met is %f" % Solution4

print "The empirical probability that coin B is showing 1 when the stopping condition is met is %f" % Solution5

