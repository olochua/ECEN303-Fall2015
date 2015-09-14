__author__ = "David Fawcett"
__NetID__ = "dgf378"
__GitHubID__ = "dfawcett"
__challenge__ = "1"
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


ParameterP = 0.3
NumberFlips = 8
NumberTrials = 100000
Trials = []


def biasedcoinflip(p=0.5):
    # EDIT
    # Create method for biased coin flip
    #
    num = random.random()
    if num < p:
        return 1
    else:
        return 0



for TrialIndex1 in range(0, NumberTrials):
    Trials.append(biasedcoinflip(ParameterP))

TrialAverage = sum(Trials) / (1.0 * len(Trials))
print 'The average number of ones is {0:.4f}.'.format(TrialAverage)

SumTrials = []

for TrialIndex2 in range(0, NumberTrials):
    # EDIT
    # Add NumberFlips coin flips for each SumTrials outcome
    #
    sum = 0
    for i in range(0, NumberFlips):
        sum += biasedcoinflip(ParameterP)
    SumTrials.append(sum)


Distribution = []
for OutcomeIndex1 in range(0, NumberFlips + 1):
    Distribution.append(SumTrials.count(OutcomeIndex1) / (1.0 * NumberTrials))

print repr(Distribution)
# EDIT
# Print the sum of the elements in Distribution
#
sum = 0
for OutcomeIndex1 in range(0, NumberFlips + 1):
    sum += Distribution[OutcomeIndex1]
print(sum)

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
The distribution shifts left when ParameterP moves towards zero and the
distribution shifts right when ParameterP moves towards 

What is the most likely outcome for ParameterP = 0.7 and NumberFlips = 8?
6 heads out of 8 flips. 

"""
