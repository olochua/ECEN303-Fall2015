__author__ = "Fletcher Watts"
__NetID__ = "augustus1994"
__GitHubID__ = "augustus1994"
__challenge__ = "2"
__version__ = "0.0"
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

def biasedgeometricflip(p = 0.5,q = 0.5):
    triumph = 0
    Atimes = 0
    Btimes = 0
    counter = 0
    while triumph == 0:
        coinA = biasedcoinflip(p)
        coinB = biasedcoinflip(q)

        if coinA == coinB:
            counter +=1
        elif (coinA + coinB == 1):
            counter += 1
            triumph = 1
            Atimes += coinA
            Btimes += coinB

    return(counter,Atimes,Btimes)
print("Part 1\n")

#Part A
Trials = []
for TrialIndex1 in range(0, NumberTrials):
    Trials.append(geometricflip(ParameterP))
Solution1 = round(Trials.count(4)/float(len(Trials)),5)
# count the number of 4's in the list of trials/ total number of trials

print("The empirical probability that the  number of flips is 4 is " + repr(Solution1) + ".")

#Part B
even = 0
for TrialIndex2 in range(0, NumberTrials):
    if Trials[TrialIndex2]%2 == 0:
        even += 1
Solutions2 = round(Trials.count(4)/float(even),5)
# count even numbers

print("The empirical probability that the number of flips is 4 conditional on number of flips being even is " + repr(Solutions2) + ".")


print("\nPart 2\n")

Trials2 = []
FinalA = 0
FinalB = 0
for TrialIndex3 in range(0, NumberTrials):
    answer = biasedgeometricflip(ParameterA,ParameterB)
    Trials2.append(answer[0])
    FinalA += answer[1]
    FinalB += answer[2]

Solution3 = round(Trials2.count(2)/float(NumberTrials),3)
Solution4 = round(FinalA/float(NumberTrials),3)
Solution5 = round(FinalB/float(NumberTrials),3)

print("The empirical probability that the number of flips is 2 is "+repr(Solution3)+ ".")

print("The empirical probability that coin A is showing 1 when the stopping condition is met is "+repr(Solution4)+ ".")

print("The empirical probability that coin B is showing 1 when the stopping condition is met is "+repr(Solution5)+ ".")


