__author__ = "Tyler Henderson"
__NetID__ = "tyler.henderson07"
__GitHubID__ = "thenderson37"
__challenge__ = "1"
__version__ = "3.4"
__grader__ = "Jui Yen Chua"
__SelfGrade__ = "4"
__PeerGrade__ = "4"

"""
Random Signals and Systems
Course: ECEN 303-502
Maximum Grade: 5pt
"""

import random
import math
import matplotlib.pyplot as plt


ParameterP = 0.7
NumberFlips = 8
NumberTrials = 100000
Trials = []


def biasedcoinflip(p=0.5):
    """"Flips a coin using a random number generator"""
    if random.random() <= p:
        return 1
    else:
        return 0


for TrialIndex1 in range(0, NumberTrials):
    Trials.append(biasedcoinflip(ParameterP))

TrialAverage = sum(Trials) / (1.0 * len(Trials))
print( 'The average number of ones is {0:.4f}.'.format(TrialAverage))

SumTrials = []

for TrialIndex2 in range(0, NumberTrials):
   temp = 0 
   
    for TrialIndex2 in range(0, NumberFlips):
        temp = temp + biasedcoinflip(ParameterP)
        
    SumTrials.append(temp)
    # Add NumberFlips coin flips for each SumTrials outcome

Distribution = []
for OutcomeIndex1 in range(0, NumberFlips + 1):
    Distribution.append(SumTrials.count(OutcomeIndex1) / (1.0 * NumberTrials))

print( repr(Distribution))
print( sum(Distribution)) #Print the sum of the elements in Distribution
#

OutcomeIndex2 = range(0, NumberFlips + 1)
num_bins = len(OutcomeIndex2)
bar_width = 0.8
XticksIndex = [(outcome + (0.5 * bar_width)) for outcome in OutcomeIndex2]
opacity = 0.4

plt.bar(OutcomeIndex2, Distribution, bar_width, alpha=opacity, color='b')
plt.xlabel("Value")
plt.ylabel("Probability")
plt.xticks(XticksIndex, OutcomeIndex2)
plt.show()

"""
Describe what happens to the figure as you vary ParameterP from zero to one.
The peak of the distribution moves from left to right as the parameter is adjusted from zero to one.

What is the most likely outcome for ParameterP = 0.7 and NumberFlips = 8?
The most likely outcome it 6 with probability of 0.3.


"""
