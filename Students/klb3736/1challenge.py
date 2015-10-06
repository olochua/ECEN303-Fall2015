_author__ = "Kaitlin Basham"
__NetID__ = "klb3736"
__GitHubID__ = "klb3736"
__challenge__ = "1"
__version__ = "1.0"
__grader__ = "Matthew Grogan"
__SelfGrade__ = "3"
__PeerGrade__ = "3"

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
    if random.random() < p:
        return 1
    else:
        return 0


for TrialIndex1 in range(0, NumberTrials):
    Trials.append(biasedcoinflip(ParameterP))

TrialAverage = sum(Trials) / (1.0 * len(Trials))
print 'The average number of ones is {0:.4f}.'.format(TrialAverage)

SumTrials = []

for TrialIndex2 in range(0, NumberTrials):
    SumTrials.append(sum(Trials.count(TrialIndex2)))

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
As ParameterP goes from zero to one, there are more outcomes of 1 and less of 0.

What is the most likely outcome for ParameterP = 0.7 and NumberFlips = 8?
In this case, there is a 0.7 probability of getting a 1 on a flip, and there are 8 flips, so there will likely be
(0.7)(8)=5.6 outcomes of 1. There cannot be 5.6 flips that produce a 1, so the most likely outcome for ParameterP=0.7
and NumberFlips is six 1s and two 0s.
"""

