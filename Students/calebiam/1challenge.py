__author__ = "Caleb Holley"
__NetID__ = "calebiam"
__GitHubID__ = "calebiam"
__challenge__ = "1"
__version__ = "3.4"
__grader__ = ""
__SelfGrade__ = "5"
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
print('The average number of ones is {0:.4f}.'.format(TrialAverage))  #changed to work with updated version of Python

SumTrials = []

for TrialIndex2 in range(0, NumberTrials):
    sum_temp = 0
    for index in range(0, NumberFlips):
        sum_temp += biasedcoinflip(ParameterP)
    SumTrials.append(sum_temp)

Distribution = []
for OutcomeIndex1 in range(0, NumberFlips + 1):
    Distribution.append(SumTrials.count(OutcomeIndex1) / (1.0 * NumberTrials))

print (repr(Distribution))  #changed to work with updated version
Distrib_Sum = 0
for item in Distribution:
    Distrib_Sum += item
print(repr(Distrib_Sum))

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

When the ParameterP is equal to zero the graph is a single bar over the 0 x-value, meaning there is zero probability of
receiving a one. As you increase the ParameterP the other x-values start generating bars above them, meaning the other
outcomes become possible. As ParameterP begins to get closer to one the likelihood of larger x-values increases and the
smaller x-values decreases. When the value of ParameterP is one the graph generates a solid bar above the x-value, 8,
meaning that out of the 8 flips all of them returned the value one. Making the probability of receiving a one, 100%.
So the figure has a kind of left to right shift depending on the value of ParameterP.

What is the most likely outcome for ParameterP = 0.7 and NumberFlips = 8?

When ParameterP is equal to 0.7 and NumberFlips equal to 8, the most likely outcome is 6 with a probability of around
0.297 or 29.7%.

"""
