__author__ = "Joshua Ruff"
__NetID__ = "joshruff"
__GitHubID__ = "joshruff"
__challenge__ = "2"
__version__ = "0.0"
__grader__ = ""
__SelfGrade__ = "5"
__PeerGrade__ = ""

#***Written Using Python 3***
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
testP = 4 #Test Parameter for gemetric flips


def biasedcoinflip(p=0.5):
#    """
#    This method returns a one with probability p and it returns a zero with
#    probability (1 - p). The default parameter is p=0.5; this can be changed
#    by passing an argument to the method.
#    """
    return math.floor(random.random() + p)


def geometricflip(p=0.5):
#    """
#    This method returns a natural number that denotes the number of digital
#    coin flips needed to obtain a one. It relies on method biasedcoinflip().
#    """
	numberflips = 1
	while biasedcoinflip(p) != 1:
		numberflips += 1
	return numberflips


print ("\n\nPart 1\n")

Trials = []
trialP_hits=0
EvenTrials = 0
for TrialIndex1 in range(0, NumberTrials):
	
	t=geometricflip(ParameterP)

	if t==testP:
		trialP_hits+=1

	if t%2==0:
		EvenTrials+=1

	Trials.append(t)


Solution1=trialP_hits/NumberTrials
Solution2=trialP_hits/EvenTrials

print("The empirical probability that the  number of flips is 4 is "  + repr(Solution1) + ".\n\n")

print ("The empirical probability that the number of \nflips is 4 conditional on number of flips being even is " + repr(Solution2)  + ".")


print ("\n\n\nPart 2\n")




Trials2 = []
FinalA = 0
FinalB = 0
twoFlips=0
for TrialIndex2 in range(0, NumberTrials):
	trialA=0
	trialB=0
	while trialA==trialB:	
		trialA+=geometricflip(ParameterA)
		trialB+=geometricflip(ParameterB)
	if trialA<trialB:
		Trials2.append(trialA)
		FinalA+=1
	else:
		Trials2.append(trialB)
		FinalB+=1
	if trialB==2 or trialA==2:
		twoFlips+=1
	
		
		
Solution3=twoFlips/NumberTrials
Solution4=FinalA/NumberTrials
Solution5=FinalB/NumberTrials

   
print ("The empirical probability that the number of flips is 2 is \n" + repr(Solution3)  + ".\n\n")

print ("The empirical probability that coin A is showing 1 when the stopping condition is \nmet is " + repr(Solution4) + ".\n\n")

print ("The empirical probability that coin B is showing 1 when the stopping condition is \nmet is " + repr(Solution5) + ".\n\n")

