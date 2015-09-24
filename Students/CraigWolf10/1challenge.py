__author__ = "Craig Wolf"
__NetID__ = "Dallascowboys10"
__GitHubID__ = "CraigWolf10"
__challenge__ = "1"
__version__ = "1.0"
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


ParameterP = 0.9
NumberFlips = 8
NumberTrials = 10000
Trials = []

TrialSequence = []
Cardinality = 2


def biasedcoinflip(p=0.5):
    for TrialIndex in range(0, NumberTrials):
        TrialSequence.append(random.randrange(Cardinality))
        if (sum(TrialSequence)/ (1.0 *len(TrialSequence))) < ParameterP:
            TrialSequence[len(TrialSequence)-1] = 1
            return 1
        else:
            TrialSequence[len(TrialSequence)-1] = 0
            return 0


for TrialIndex1 in range(0, NumberTrials):
    Trials.append(biasedcoinflip(ParameterP))



TrialAverage = sum(Trials) / (1.0 * len(Trials))
print 'The average number of ones is {0:.4f}.'.format(TrialAverage)


SumTrials = []

for TrialIndex2 in range(0, NumberTrials):
    countflips = []
    for TrialIndex3 in range(0, NumberFlips):
        countflips.append(biasedcoinflip(ParameterP))
    SumTrials.append(sum(countflips))


Distribution = []
for OutcomeIndex1 in range(0, NumberFlips + 1):
    Distribution.append(SumTrials.count(OutcomeIndex1) / (1.0 * NumberTrials))

print repr(Distribution)
print sum(Distribution)

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

As ParameterP is varied from zero to one the most likely outcome changes from being
a low number at low values of ParameterP, to high numbers at high values of ParameterP.
For example, at ParameterP = 0.1 the most likely outcome is 1, while at ParameterP = 0.9,
the most likely outcome is 7.

What is the most likely outcome for ParameterP = 0.7 and NumberFlips = 8?

The most likely outcome under these circumstances is 6.

"""
