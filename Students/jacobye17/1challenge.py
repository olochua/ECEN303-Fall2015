__author__ = "Jacoby Prestwood"
__NetID__ = "jacobye17"
__GitHubID__ = "jacobye17"
__challenge__ = "1"
__version__ = "1.0.1"
__grader__ = ""
__SelfGrade__ = "2"
__PeerGrade__ = ""

"""
Random Signals and Systems
Course: ECEN 303-502
Maximum Grade: 5pt
"""

import random
import math
import matplotlib.pyplot as plt


ParameterP = 0.3
NumberFlips = 8
NumberTrials = 100000
Trials = []

def biasedcoinflip(p=0.5):
    # EDIT
    # Create method for biased coin flip
    # Gives you a 0 with probability p and 1 otherwise
    if random.random() < p:
        return 0
    else:
        return 1


for TrialIndex1 in range(0, NumberTrials):
    Trials.append(biasedcoinflip(ParameterP))

TrialAverage = sum(Trials) / (1.0 * len(Trials))
print 'The average number of ones is {0:.4f}.'.format(TrialAverage)

SumTrials = []

# define some variable "val" is equal to 0
val = 0
for TrialIndex2 in range(0, NumberTrials):
    # EDIT
    # Add NumberFlips coin flips for each SumTrials outcome
    # This creates a loop that adds the number of flips to the number of trials
    for TrialIndex2 in range(0,NumberFlips):
        val += biasedcoinflip(ParameterP)
    SumTrials.append(val)
    val = 0

Distribution = []
for OutcomeIndex1 in range(0, NumberFlips + 1):
    Distribution.append(SumTrials.count(OutcomeIndex1) / (1.0 * NumberTrials))

sum = 0
print repr(Distribution)
# EDIT
# Print the sum of the elements in Distribution
# All this does is add some number from the distribution to a variable and then prints it to show that the total
# probability of the experiment is 1
for value in Distribution:
    sum += value

print("Sum of the elements in Ditribution: ") + str(sum)

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
The center of the distribution will shift along the x-axis. As ParameterP goes from zero to one the center will move
from left to right on the x-axis.

What is the most likely outcome for ParameterP = 0.7 and NumberFlips = 8?
Most likely outcome is 6

"""
