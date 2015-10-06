from __future__ import division
__author__ = "Matt Grogan"
__NetID__ = "grogan2122"
__GitHubID__ = "mdgrogan"
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


print "Part 1\n"

#Trials = [] not using
Solution1 = 0
for TrialIndex1 in range(0, NumberTrials):
	gf = geometricflip(ParameterP)
#	Trials.append(geometricflip(ParameterP))
	if gf == 4.0000:	#counting four flip trials
		Solution1 += 1

Solution1 /= NumberTrials

print 'The empirical probability that the  number of flips is 4 is ' + repr(Solution1) + '.'

EvenTrials = 0
Solution2 = 0
for TrialIndex2 in range(0, NumberTrials):
	gf = geometricflip(ParameterP)
	if gf%2 == 0:	#counting even trials
		EvenTrials += 1
		if gf == 4.0000:	#counting four flip trials
			Solution2 += 1

Solution2 /= EvenTrials

print "The empirical probability that the number of flips is 4 conditional on number of flips being even is {0:.4f}.".format(Solution2)


print "\nPart 2\n"

#Trials2 = []
FinalA = 0
FinalB = 0
Solution3 = 0
for TrialIndex2 in range(0, NumberTrials):
	numflips = 0
	bf1 = 0
	bf2 = 0
	while bf1 == bf2:
		numflips += 1
		bf1 = biasedcoinflip(ParameterA)
		bf2 = biasedcoinflip(ParameterB)
	if numflips == 2:	#counting two flip trials
			Solution3 += 1
	FinalA += bf1
	FinalB += bf2

Solution3 /= NumberTrials
Solution4 = FinalA / NumberTrials
Solution5 = FinalB / NumberTrials

print "The empirical probability that the number of flips is 2 is " \
	+ repr(Solution3) \
	+ "."
print "The empirical probability that coin A is showing 1 when the stopping condition is met is " \
	+ repr(Solution4) \
	+ "."
print "The empirical probability that coin B is showing 1 when the stopping condition is met is " \
	+ repr(Solution5) \
	+ "."


