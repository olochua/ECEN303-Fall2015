__author__ = 'Colbie'
author__ = "Colbie Prestwood"
__NetID__ = "cprestwood2012"
__GitHubID__ = "cprestwood2012"
__challenge__ = "1"
__version__ = "3.4"
__grader__ = ""
__SelfGrade__ = "4"
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

    if random.random() <= p:
        return 1  # 1 meaning the statement is true
    else:
        return 0  # 0 nmeaning the statement is  false


for TrialIndex1 in range(0, NumberTrials):
    Trials.append(biasedcoinflip(ParameterP))

TrialAverage = sum(Trials) / (1.0 * len(Trials))
print('The average number of ones is {0:.4f}.'.format(TrialAverage))

SumTrials = []

for TrialIndex2 in range(0, NumberTrials):
    
    # Add NumberFlips coin flips for each SumTrials outcome
    Temp = 0  #this represents a temporary sum to perform the neccesary functions
    for InnerIndex in range(0, NumberFlips):
        Temp += biasedcoinflip(ParameterP)
    SumTrials.append(Temp)


Distribution = []
for OutcomeIndex1 in range(0, NumberFlips + 1):
    Distribution.append(SumTrials.count(OutcomeIndex1) / (1.0 * NumberTrials))

# Print the sum of the elements in Distribution
print(repr(Distribution))
SumDistribution = 0  #this term allows for allocated space to print.
for item in Distribution:
    SumDistribution += item
print(repr(SumDistribution))

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

A shift in the graph from left to right will occur as the value increases from zero to one. At zero the graph will show no rise in the bar and then at one a rise in the bar will occur and then simiar occurences shall happen as the ParameterP value increases.
What is the most likely outcome for ParameterP = 0.7 and NumberFlips = 8?

At ParameterP  equal to 0.7 and NumberFlips equal to 8, the outcome should come out to 6 with a probability of roughly
30%.

"""
