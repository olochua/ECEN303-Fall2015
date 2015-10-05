__author__ = "Fernando Romo"
__NetID__ = "jfernandoromoddl"
__GitHubID__ = "FernandoRomo"
__challenge__ = "1"
__version__ = "Python 2.7"
__grader__ = ""
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
    # EDIT 1
    # Create method for biased coin flip
    if random.random()<p:
        return 1 #Probability of Heads 0.5, Heads = 1 (True)

    else:
        return 0 #Probability of Tails 0.5, Tails = 0 (False)

for TrialIndex1 in range(0, NumberTrials):
    Trials.append(biasedcoinflip(ParameterP))

TrialAverage = sum(Trials) / (1.0 * len(Trials))
print 'The average number of ones is {0:.4f}.'.format(TrialAverage)

SumTrials = []

HeadsSum = 0 #Initialize the sum of Heads to zero. ( Heads: value is equal to 1)
for TrialIndex2 in range(0, NumberTrials):
    # EDIT 2
    # Add NumberFlips coin flips for each SumTrials outcome
    for index in range(0, NumberFlips): #Range to sum all the coin flips
        HeadsSum = HeadsSum + biasedcoinflip(ParameterP) #Sum of all the actual flips

    SumTrials.append(HeadsSum) #Return the answer of the sum
    HeadsSum = 0 #Restore the Counter of Heads to zero.

Distribution = []
for OutcomeIndex1 in range(0, NumberFlips + 1):
    Distribution.append(SumTrials.count(OutcomeIndex1) / (1.0 * NumberTrials))

print repr(Distribution)
# EDIT 3
# Print the sum of the elements in Distribution
print sum(Distribution) #Prints the actual Distribution

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
>> When you increase the ParameterP from zero to one, the Probability Distribtuion moves
from the left to the right. Therefore, the Number of Flips to get a (Head = 1) increases
as the ParameterP increases in the interval (0,1).

What is the most likely outcome for ParameterP = 0.7 and NumberFlips = 8?
>>The most likely outcome for the given parameters is 6 with a Probability of about 30%.
"""
