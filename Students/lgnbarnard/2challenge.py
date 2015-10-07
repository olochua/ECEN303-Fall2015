__author__ = "Logan Barnard"
__NetID__ = "lgn_barnard"
__GitHubID__ = "lgnbarnard"
__challenge__ = "2"
__version__ = "1.0"
__grader__ = ""
__SelfGrade__ = "5"   #Almost positive everything is in working order, solutions seem to be correct
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
NumberTrials = 100000   #number of total trials


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


print ("Part 1\n")

Trials = []
Prob4 = 0
for TrialIndex1 in range(0, NumberTrials):         #for all trials
    Trials.append(geometricflip(ParameterP))
    if Trials[TrialIndex1] == 4:                   #if the trial is a 4
        Prob4 += 1.0                               #then count 1

Solution1 = Prob4 / NumberTrials                   #probability of a 4

print ("The empirical probability that the  number of flips is 4 is " + repr(Solution1) + ".") #pring prob of a 4

EvenTrials = 0
for TrialIndex2 in range(0, NumberTrials):         #for all trials
    if Trials[TrialIndex2] % 2 == 0:               #if its divisible by 2 with no remainers
        EvenTrials += 1.0                          #then count 1
ProbEven = EvenTrials / NumberTrials
Solution2 = Solution1 / ProbEven                   #probability of 4 with even numbers

print ("The empirical probability that the number of flips is 4 conditional on number of flips being even is " \
      + repr(Solution2) + ".")


print "\nPart 2\n"

Trials2 = []
P2 = 0
PA = 0               #setting variabls for probability solutions
PB = 0
for TrialIndex2 in range(0, NumberTrials):
    FinalA = 0
    FinalB = 0              #more variabls
    Flips = 0
    while FinalA == FinalB:
        FinalA = biasedcoinflip(ParameterA)
        FinalB = biasedcoinflip(ParameterB)
        Flips += 1                                  #While FinalA = FinalB keep adding flips
    Trials2.append(Flips)
    if Trials2[TrialIndex2] == 2:       #if 2 is rolled add to P2
        P2 += 1.0
    if FinalA == 1:
        PA += 1.0
    if FinalB == 1:
        PB += 1.0

Solution3 = P2 / NumberTrials
Solution4 = PA / NumberTrials
Solution5 = PB / NumberTrials

print ("The empirical probability that the number of flips is 2 is " + repr(Solution3) + ".")

print ("The empirical probability that coin A is showing 1 when the stopping condition is met is " \
      + repr(Solution4) + ".")

print ("The empirical probability that coin B is showing 1 when the stopping condition is met is " \
      + repr(Solution5) + ".")
