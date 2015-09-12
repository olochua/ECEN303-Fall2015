__author__ = "Allison Badgett"
__NetID__ = "allisonbadgett"
__GitHubID__ = "allisonbadgett"
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


ParameterP = 0.7
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
print('The average number of ones is {0:.4f}.'.format(TrialAverage)) #altered from original to work with Python 3.4

SumTrials = []

for TrialIndex2 in range(0, NumberTrials):
    TempSum = 0
    for InnerIndex in range(0, NumberFlips):
        TempSum += biasedcoinflip(ParameterP)
    SumTrials.append(TempSum)

Distribution = []
for OutcomeIndex1 in range(0, NumberFlips + 1):
    Distribution.append(SumTrials.count(OutcomeIndex1) / (1.0 * NumberTrials))

print(repr(Distribution)) #altered from original to work with Python 3.4
SumDistrib = 0
for item in Distribution:
    SumDistrib += item
print(repr(SumDistrib))

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

The figure shifts from the left to the right as the probability of receiving a one becomes more likely.
This makes sense intuitively because the the probability of receiving a one gets higher, the number of ones 
received per trial should increase. When ParameterP is zero, the graph is a single bar over
the 0 x-value. This makes sense as there is zero probability of receiving a one. When ParameterP increases, 
other outcomes become possible. As ParameterP increases, the likelihood of larger x-values increases and 
the likelihood of smaller x-values decreases. When ParameterP is 0.5, the graph is the most 
balanced. It should be a practically symmetrical pyramid. As ParameterP increases to one, smaller 
x-values become less likely. When ParameterP is 1, the graph is a single bar over the 8 x-value. This 
means that all coin flips returned a 1. This makes sense because the probabality of receiving a one is 1, 
or 100%.

What is the most likely outcome for ParameterP = 0.7 and NumberFlips = 8?

The most likely outcome is 6 with a probability of about .296 (29.6%).

"""
