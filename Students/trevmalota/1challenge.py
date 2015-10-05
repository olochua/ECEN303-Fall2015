__author__ = "Trevor Malota"
__NetID__ = "TrevorMalota"
__GitHubID__ = "trevmalota"
__challenge__ = "1"
__version__ = "2.7"
__grader__ = ""
__SelfGrade__ = "3"
__PeerGrade__ = "2"

"""
Random Signals and Systems
Course: ECEN 303-502
Maximum Grade: 5pt
"""

import random
import math
import matplotlib.pypl


ParameterP = 0.3
NumberFlips = 8
NumberTrials = 100000
Trials = []


def biasedcoinflip(p=0.5):
    if random.random() <= p:
        return 1
    else:
        return 0

for TrialIndex1 in range(0, NumberTrials):
    Trials.append(biasedcoinflip(ParameterP))

TrialAverage = sum(Trials) / (1.0 * len(Trials))
print 'The average number of ones is {0:.4f}.'.format(TrialAverage)

SumTrials = []

for TrialIndex2 in range(0, NumberTrials):
        sumNumberFlips = 0
for TrialIndex in range(0, NumberFlips):
        sumNumberFlips += biasedcoinflip(ParameterP)
SumTrials.append(sumNumberFlips)

Distribution = []
for OutcomeIndex1 in range(0, NumberFlips + 1):
    Distribution.append(SumTrials.count(OutcomeIndex1) / (1.0 * NumberTrials))

print repr(Distribution)
SumDistribution = 0
SumDistribution = sum(Distribution)
print repr(SumDistribution)


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

The figure shifts left to right

What is the most likely outcome for ParameterP = 0.7 and NumberFlips = 8?

The most likely outcome is 6

"""
