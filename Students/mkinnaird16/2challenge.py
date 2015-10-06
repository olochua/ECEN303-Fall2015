__author__ = ""
__NetID__ = ""
__GitHubID__ = ""
__challenge__ = "2"
__version__ = "1.4"
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

fourprobability = round(Trials.count(4)/float(len(Trials)),5)
#divide by the number of trials from the # of 4's in the traisl

print "The empirical probability that the  number of flips is 4 is " + repr(fourprobability) + "."

EvenTrials = 0
for TrialIndex2 in range(0, NumberTrials):
    if Trials[TrialIndex2]%2 == 0: 
        EvenTrials =+ 1 #trails will be a mulitple of 2
evenprobability = round(Trials.count(4)/float(EvenTrials),5)

print "The empirical probability that the number of flips is 4 conditional on number of flips being even is " 
 
    + "."


print "\nPart 2\n"

def GeometricFlipBiased(p=0.5, q=0.5):
    contol1 = 0
    countA = 0
    countB = 0
    count = 0
    
    while contol1 == 0:
        coinA = biasedcoinfip(p)
        coinB = biasedcoinflip(q)
        
        if coinA == coinB:
            count += 1
            countA += coinA
            countB += coinB
            contol1 = 1
            
    return(count,countA,countB)
    
Trials2 = []
FinalA = 0
FinalB = 0
for TrialIndex2 in range(0, NumberTrials):
    GeometircResult = GeometricFlipBiased(ParameterA,ParameterB)
    Trials2.append(GeometicResult[0]}
    FinalA += GeometricResult[1]
    FinalB += GeometricResult[2]
    
    Probability2 = round(Trials2.count(2)/float(NumberTrials),3)
    CoinAlpha = round(FinalA/ float(NumberTrials),3)
    CoinBeta = round(FinalB/ float(NumberTrials),3)
print "The empirical probability that the number of flips is 2 is " + repr(Probability2) + ".")
    
print "The empirical probability that coin A is showing 1 when the stopping condition is met is " + repr(coinAlpha) + ".")
 
print "The empirical probability that coin B is showing 1 when the stopping condition is met is " + repr(coinBeta) + ".")
    # EDIT: + repr(Solution5)) \
    + "."

