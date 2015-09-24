__author__ = "Morgan Frakes"
__NetID__ = "mgfrakes13"
__GitHubID__ = "mgfrakes"
__challenge__ = "1"
__version__ = "1.0"
__grader__ = ""
__SelfGrade__ = "5pts"
__PeerGrade__ = ""

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
    probability = random.random()
    if probability <= p:
        return 1
    else:
        return 0

for TrialIndex1 in range(0, NumberTrials):
    Trials.append(biasedcoinflip(ParameterP))

TrialAverage = sum(Trials) / (1.0 * len(Trials))
print 'The average number of ones is {0:.4f}.'.format(TrialAverage)

SumTrials = []
x = 0

for TrialIndex2 in range(0, NumberTrials):
    if (TrialIndex2 + 1) % 8 == 0:
        SumTrials.append(x)
        x = 0
    x += Trials[TrialIndex2]

Distribution = []
for OutcomeIndex1 in range(0, NumberFlips + 1):
    Distribution.append(SumTrials.count(OutcomeIndex1) / (1.0 * NumberTrials))

print repr(Distribution)
z = 0
for i in range(0, len(Distribution)):
    z += Distribution[i]
print "The sum of the distribution is " + str(z)

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

As we vary ParameterP, the figure changes the probability accordingly of getting between 1 and 8 flips in a row.
The lower ParameterP, the probability is higher for fewer flips and vice versa.


What is the most likely outcome for ParameterP = 0.7 and NumberFlips = 8?

The most likely outcome under these conditions is 6 flips in a row occurring.

"""
