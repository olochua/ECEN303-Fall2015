__author__ = "Weston Torti"
__NetID__ = "tort115"
__GitHubID__ = "westort"
__challenge__ = "1"
__version__ = "0.0"
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

ParameterP = 0.7
NumberFlips = 8
NumberTrials = 100000
Trials = []
TrialSum = 0


def biasedcoinflip(p=0.5):
    if random.random() <= p:  # gives probability with value of parameter p
        return 1
    else:  # since random goes from 0 to 1 else will give 0's with value 1-p
        return 0


for TrialIndex1 in range(0, NumberTrials):
    Trials.append(biasedcoinflip(ParameterP))

TrialAverage = sum(Trials) / (1.0 * len(Trials))
print 'The average number of ones is {0:.4f}.'.format(TrialAverage)
SumTrials = []
for TrialIndex2 in range(0, NumberTrials):#going through each trial
    CoinSum = 0
    for TrialIndex3 in range(0, NumberFlips):#going through each flip per trial
        CoinSum += biasedcoinflip(ParameterP)
    SumTrials.append(CoinSum) #appending the most recent trials sum to the trial sum

Distribution = []
for OutcomeIndex1 in range(0, NumberFlips + 1):
    Distribution.append(SumTrials.count(OutcomeIndex1) / (1.0 * NumberTrials))


DistributionSum= 0
DistributionSum = sum(Distribution)
print repr(Distribution)
print repr(DistributionSum)

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
As ParameterP is varied from zero to one, The figure is shifted from left to right along the x axis, this is because
the probability for getting a one is becoming more and more likely therefore increasing the count of 1's in a trial

What is the most likely outcome for ParameterP = 0.7 and NumberFlips = 8?

The most likely outcome with the given inputs is 6
"""
