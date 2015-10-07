__author__ = "Jui Yen Chua"
__NetID__ = "olochua"
__GitHubID__ = "olochua"
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


print ("Part 1\n")

#vector that stores all the trials
Trials = []
#variable that indicates when the number of flips is 4
flip_is_four = 0  

for TrialIndex1 in range(0, NumberTrials):
    Trials.append(geometricflip(ParameterP))

    #if the number of flips is 4, increment the counter
    if Trials[TrialIndex1] == 4:
        flip_is_four = flip_is_four + 1

print ("The empirical probability that the  number of flips is 4 is " + repr(flip_is_four/NumberTrials) 
    + ".")

#condition: event occurs on even flips
EvenTrials = 0
for TrialIndex2 in range(0, NumberTrials):

    #compute the condition of even flips 
    if Trials[TrialIndex2] % 2 == 0:
        EvenTrials = EvenTrials + 1
        

print ("The empirical probability that the number of flips is 4 conditional on number of flips being even is " + repr(flip_is_four/EvenTrials)
    + ".")


print ("\nPart 2\n")

Trials2 = []
FinalA = 0
FinalB = 0

flip_is_two = 0
for TrialIndex2 in range(0, NumberTrials):
    #performs coin flips
    coin_A = geometricflip(ParameterA)
    coin_B = geometricflip(ParameterB)

    #if coin B is stopping the experiment
    if coin_A > coin_B:
        Trials2.append(coin_B)
        FinalB = FinalB + 1
    #if coin A is stopping the experiment
    elif coin_A < coin_B:
        Trials2.append(coin_A)
        FinalA = FinalA + 1
    #if both coins are stopping the experiment
    else:
        Trials2.append(coin_A)
        FinalA = FinalA + 1
        FinalB = FinalB + 1

#if the number of flips is 2, increment the counter
for TrialIndex2 in range(0, NumberTrials):
    if Trials2[TrialIndex2] == 2:
        flip_is_two = flip_is_two + 1    

print ("The empirical probability that the number of flips is 2 is " + repr(flip_is_two/NumberTrials)
    + ".")
print ("The empirical probability that coin A is showing 1 when the stopping condition is met is " + repr(FinalA/NumberTrials)
    + ".")
print ("The empirical probability that coin B is showing 1 when the stopping condition is met is " + repr(FinalB/NumberTrials)
    + ".")

