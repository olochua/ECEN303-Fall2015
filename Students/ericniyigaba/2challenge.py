__author__ = "Eric Niyigaba"
__NetID__ = "124009735"
__GitHubID__ = "ericniyigaba"
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
Numberflis = 0 # parameter to keep track of number of flips

def biasedcoinflip(p=0.5):       # initialized funcition to p=0.5
    if random.random() < (1-p):  # 0 is returned by this codes when random value is < 1-p
        return 0
    else:                        # 1 is returned otherwise
        return 1


def geometricflip(p=0.5):
    """
    This method returns a natural number that denotes the number of digital
    coin flips needed to obtain a one. It relies on method biasedcoinflip().
    """
    numberflips = 1
    while biasedcoinflip(p) != 1:   # when this function did not return 1
        numberflips += 1            # store each time in mumberflips current value + 1
    return numberflips              # totoal number of flips are returned 

print("Part 1\n")       # just for clarification 

Trials = []         # array to store number of flips at each run
for TrialIndex1 in range(0, NumberTrials):      # for loop that run number of trials 
    Trials.append(geometricflip(ParameterP))    # pass ParameterP to geometricflip
Solution1 = Trials.count(4)/len(Trials)         # numuber of trials are stored in variable sulution1

# Print the result for the number of 4's that occurred
print("The empirical probability that the  number of flips is 4 is " + repr(Solution1) + ".")

EvenTrials = 0            # to store number of even trials
for item in Trials:       # run number of available trials 
    if item % 2 == 0:     # check if number is even
        EvenTrials += 1   # save evenTrials + 1
Solution2 = Trials.count(4)/EvenTrials      

# Print the solution to the second section of Part 1
print('The empirical probability that the number of flips is 4 conditional on number of flips being even is {0:.6f}.' \
      .format(Solution2))

print("\nPart 2\n")         # second clarification 

FinalA = 0          
FinalB = 0         
Flip2 = 0          
for TrialIndex2 in range(0, NumberTrials):      
    FlipA = 0       
    FlipB = 0 
    Flips = 0       
    while FlipA == FlipB:       # while A and B holds the same value
        FlipA = biasedcoinflip(ParameterA)      # Flip coin A
        FlipB = biasedcoinflip(ParameterB)      # Flip coin B
        Flips += 1              # 1 is added to Flips
    FinalA += FlipA             # 1 is added to FinalA 
    FinalB += FlipB             # 1 is added to FinalB
    if Flips == 2:              # if Flips = 2 , add 1 to Fli
        Flip2 += 1

FinalA /= NumberTrials         
FinalB /= NumberTrials         
Flip2 /= NumberTrials           


print('The empirical probability that the number of flips is 2 is {0:.6f}.' \
      .format(Flip2))

print('The empirical probability that coin A is showing 1 when the stopping condition is met is {0:.6f}.' \
      .format(FinalA))

print('The empirical probability that coin B is showing 1 when the stopping condition is met is {0:.6f}.' \
      .format(FinalB))

#END :)
