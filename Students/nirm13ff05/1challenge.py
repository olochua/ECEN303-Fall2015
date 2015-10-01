__author__ = "Nirmal Patel"
__NetID__ = "nirm13ff05"
__GitHubID__ = "nirm13ff05"
__challenge__ = "1"
__version__ = "2.7"
__grader__ = "Colbie Prestwood"
__SelfGrade__ = "3"
__PeerGrade__ = "5"

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
    TempSum = 0
    for add_Number in range(0, NumberFlips):
        TempSum += biasedcoinflip(ParameterP)
    SumTrials.append(TempSum)

Distribution = []
for OutcomeIndex1 in range(0, NumberFlips + 1):
    Distribution.append(SumTrials.count(OutcomeIndex1) / (1.0 * NumberTrials))

print repr(Distribution)
Dis_Sum = 0
for item in Distribution:
    Dis_Sum += item
print(repr(Dis_Sum))

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

The increase of ParameterP from 0 to 1 causes the figure to go from left to right along the x-axis of the graph. Ultimately 
as the ParameterP value increases towards one the distribution will be more even across the graph.  

What is the most likely outcome for ParameterP = 0.7 and NumberFlips = 8?

Outcome = 6
Probability = ~30%


"""
