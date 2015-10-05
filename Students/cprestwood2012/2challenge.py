__author__ = "Colbie Prestwood"
__NetID__ = "cprestwood2012"
__GitHubID__ = "cprestwood2012"
__challenge__ = "2"
__version__ = "3.4"
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
Trial1      = 4
Trial2      = 2


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

def doubleflip(p1=0.5 , p2= 0.5):
    numberflips = 1
    count1 = 0
    count2 = 0
    
    while (1):
        coin1 = biasedcoinflip(p1)
        coin2 = biasedcoinflip(p2)
        if (coin1 == coin2):
            numberflips += 1 s
        else:
                break
    if(coin1):
        count1 += 1
    elif(coin2):
         count2 += 1
     else:
       break
     return (numberflips, count1, count2)
     
        

print "Part 1\n"

Trials = []
for TrialIndex1 in range(0, NumberTrials):
    Trials.append(geometricflip(ParameterP))
#
# EDIT
#

print "The empirical probability that the  number of flips is 4 is " \
    # EDIT: + repr(Solution1)) \
    + "."

EvenTrials = 0
for TrialIndex2 in range(0, NumberTrials):
    #
    # EDIT
    #

print "The empirical probability that the number of flips is 4 conditional on number of flips being even is " \
    # EDIT: + repr(Solution2)) \
    + "."


print "\nPart 2\n"

Trials2 = []
FinalA = 0
FinalB = 0
for TrialIndex2 in range(0, NumberTrials):
    #
    # EDIT
    #

print "The empirical probability that the number of flips is 2 is " \
    # EDIT: + repr(Solution3)) \
    + "."
print "The empirical probability that coin A is showing 1 when the stopping condition is met is " \
    # EDIT: + repr(Solution4)) \
    + "."
print "The empirical probability that coin B is showing 1 when the stopping condition is met is " \
    # EDIT: + repr(Solution5)) \
    + "."

