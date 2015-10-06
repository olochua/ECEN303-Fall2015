__author__ = "Mirel Duka"
__NetID__ = "iDuka"
__GitHubID__ = "iDuka"
__challenge__ = "1"
__version__ = "0.9"
__grader__ = "Stephanie Demco"
__SelfGrade__ = "2"
__PeerGrade__ = "2"

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
    #Edit
    if random.random() < p:
        return 1
    else:
        return 0


for TrialIndex1 in range(0, NumberTrials):
    Trials.append(biasedcoinflip(ParameterP))

TrialAverage = sum(Trials) / (1.0 * len(Trials))
print ('The average number of ones is {0:.4f}.'.format(TrialAverage))

SumTrials = []

for TrialIndex2 in range(0, NumberTrials):
    #Edited
    sum_i = 0
    for ind in range(0,NumberFlips):
        sum_i += biasedcoinflip(ParameterP)
    SumTrials.append(sum_i)

Distribution = []
for OutcomeIndex1 in range(0, NumberFlips + 1):
    Distribution.append(SumTrials.count(OutcomeIndex1) / (1.0 * NumberTrials))

print(repr(Distribution))
# EDIT
# Print the sum of the elements in Distribution
dist_sum = sum(Distribution)
print("The Sum of the distributions is %d" % dist_sum)

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
What is the most likely outcome for ParameterP = 0.7 and NumberFlips = 8?
"""
