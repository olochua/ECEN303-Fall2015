__author__ = "Andrew Douglass"
__NetID__ = "adoulgas"
__GitHubID__ = "ajdouglass"
__challenge__ = "2"
__version__ = "1.0"
__grader__ = ""
__SelfGrade__ = "5pt"
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
NumberTrials = 100000   # Total number of trials


def biasedcoinflip(p=0.5):       # define method, give default value to p
    if random.random() < (1-p):  # generate random number between 0 and 1, if it is less than 1-p, return 0
        return 0
    else:                        # otherwise return 1
        return 1


def geometricflip(p=0.5):
    """
    This method returns a natural number that denotes the number of digital
    coin flips needed to obtain a one. It relies on method biasedcoinflip().
    """
    numberflips = 1
    while biasedcoinflip(p) != 1:   # As long as the coin flip does not come up as a 1
        numberflips += 1            # Add to the total number of flips
    return numberflips              # Return the number of flips that occurred


print("Part 1\n")       # Denote the start of Part 1

Trials = []         # Hold the number of flips for each trial in a list
for TrialIndex1 in range(0, NumberTrials):      # Iterate NumberTrials times
    Trials.append(geometricflip(ParameterP))    # Add the trial for geometric flips with ParameterP
Solution1 = Trials.count(4)/len(Trials)         # Divide the number of trials that came up 4 with
                                                # total number of trials

# Print the result for the number of 4's that occurred
print("The empirical probability that the  number of flips is 4 is " + repr(Solution1) + ".")

EvenTrials = 0            # hold the total number of trials that ended in an even number of flips
for item in Trials:       # iterate through each item in Trials
    if item % 2 == 0:     # if number of flips was even
        EvenTrials += 1   # Add one to the number of even trials
Solution2 = Trials.count(4)/EvenTrials      # divide the number of 4's by the number of even trials

# Print the solution to the second section of Part 1
print('The empirical probability that the number of flips is 4 conditional on number of flips being even is {0:.6f}.' \
      .format(Solution2))

print("\nPart 2\n")         # Denote the start of Part 2

FinalA = 0          # Hold the number of times that A was 1 and ended the trial
FinalB = 0          # Hold the number of times that C was 1 and ended the trial
Flip2 = 0           # Hold the number of times it took only 2 flips
for TrialIndex2 in range(0, NumberTrials):      # iterate NumberTrials times
    FlipA = 0       # Set the result of flipping coin A
    FlipB = 0       # Set the result of flipping coin B
    Flips = 0       # Hold total number of Flips that occurred
    while FlipA == FlipB:       # while A and B are 0 or A and B are 1
        FlipA = biasedcoinflip(ParameterA)      # Flip coin A
        FlipB = biasedcoinflip(ParameterB)      # Flip coin B
        Flips += 1              # Increment number of flips
    FinalA += FlipA             # If A came up 1 then increment A
    FinalB += FlipB             # If B came up 1 then increment B
    if Flips == 2:              # If the number of flips was 2 then add one to keep count
        Flip2 += 1

FinalA /= NumberTrials          # Divide times A came up 1 by the total number of trials
FinalB /= NumberTrials          # Divide times B came up 1 by the total number of trials
Flip2 /= NumberTrials           # Divide times it took 2 flips by the total number of trials

# Print the number of number of times it took 2 flips
print('The empirical probability that the number of flips is 2 is {0:.6f}.' \
      .format(Flip2))
# Print the number of times that A came up 1 and caused the trials to stop
print('The empirical probability that coin A is showing 1 when the stopping condition is met is {0:.6f}.' \
      .format(FinalA))
# Print the number of times that B came up 1 and caused the trials to stop
print('The empirical probability that coin B is showing 1 when the stopping condition is met is {0:.6f}.' \
      .format(FinalB))

