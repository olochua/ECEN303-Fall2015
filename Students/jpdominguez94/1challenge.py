__author__ = "Jose Pablo Dominguez"
__NetID__ = "jpdominguez94"
__GitHubID__ = "jpdominguez94"
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


ParameterP = .9
NumberFlips = 8
NumberTrials = 100000
Trials = []


def biasedcoinflip(p=0.5):     #function to create the biased coin flips
    if random.random() < p:
        return 1
    else: 
        return 0

for TrialIndex1 in range(0, NumberTrials):     #Add the biased coin flips to the matrix
    Trials.append(biasedcoinflip(ParameterP))

TrialAverage = sum(Trials) / (1.0 * len(Trials)) #calculate the average number of ones
print 'The average number of ones is {0:.4f}.'.format(TrialAverage)

SumTrials = []

for TrialIndex2 in range(0, NumberTrials):
    TempSum = 0
    for InnerIndex in range(0, NumberFlips):
        TempSum += biasedcoinflip(ParameterP)
    SumTrials.append(TempSum)

Distribution = []
for OutcomeIndex1 in range(0, NumberFlips + 1):
    Distribution.append(SumTrials.count(OutcomeIndex1) / (1.0 * NumberTrials))

print repr(Distribution)
Sum_Distribution = 0
for disp_elements in Distribution:
    Sum_Distribution += disp_elements
print repr(Sum_Distribution)

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

*As the value of ParameterP increases so does the probability of getting higher
*numbers. The graphs therefore shifts to the right. When ParameterP is equal to 
*zero, however, the full bar remains in 0 since there is no probability to get 
*anything higher than that. Finally, when ParameterP is equal to 1, the bar is 
*fully in 8 since there is a hundred percent probability.

What is the most likely outcome for ParameterP = 0.7 and NumberFlips = 8?

*Based on experimental data and logic, the most likely outcome will be 6


"""
