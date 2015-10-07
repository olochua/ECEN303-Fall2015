__author__ = "Stephen Sattler"
__NetID__ = "stephensattler"
__GitHubID__ = "bogolog"
__challenge__ = "2"
__version__ = "0.0"
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
    PrFour = round(Trials.count(4)/float(len(Trials)),5)

print "The empirical probability that the  number of flips is 4 is " + repr(PrFour) +" \

EvenTrials = 0
for TrialIndex2 in range(0, NumberTrials):
   If Trials[TrialIndex2]%2 == 0:
    EvenTrials += 1
PrEven= round(Trials.count(4)/float(EvenTrials),5)

print "The empirical probability that the number of flips is 4 conditional on number of flips being even is " \
    print (repr(PrEven) + "."


print "\nPart 2\n"

Trials2 = []
FinalA = 0
FinalB = 0
for TrialIndex2 in range(0, NumberTrials):
    
    if countA1==coinB1
        count += 1
    elif (coinA1+coinB1==1
    count +=1
    countA +=1 coinA1
    countB +=1 coinB1
    
    return(count,countA,countB)

print "The empirical probability that the number of flips is 2 is " \
    " + repr(prTwo) + ".")
print "The empirical probability that coin A is showing 1 when the stopping condition is met is " \
    " + repr(CoinC) + ".")
print "The empirical probability that coin B is showing 1 when the stopping condition is met is " \
    " + repr(CoinD) + ".")

