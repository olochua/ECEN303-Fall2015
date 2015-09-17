__author__ = "Stephen Sattler"
__NetID__ = "stephensattler"
__GitHubID__ = "bogolog"
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


ParameterP = 0.3
NumberFlips = 8
NumberTrials = 100000
Trials = []


def BiasedCoinFlip(p=0.5):
    if random.random() <p:
        return 1
        else:
            return 0


for TrialIndex1 in range(0, NumberTrials):
    Trials.append(BiasedCoinFlip(ParameterP))

TrialAverage = sum(Trials) / (1.0 * len(Trials))
print 'The average number of ones is {0:.4f}.'.format(TrialAverage)

SumTrials = []

for TrialIndex2 in range(0, NumberTrials):
   TempSum = 0
   for InnerIndex in range(0, NumberFlips):
        TempSum += BiasedCoinFlip(parameterP)
        SumTrials.append(TempSum)

Distribution = []
for OutcomeIndex1 in range(0, NumberFlips + 1):
    Distribution.append(SumTrials.count(OutcomeIndex1) / (1.0 * NumberTrials))

print repr(Distribution)
Sum_Distributoin = 0
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

At zero, everything is zero because there is zero probability to get anything higher.
When ParameterP goes up, it directly corelates to the probability of getting a higher number.
At one, the bar is set to eight due to the hundred percent probability.

What is the most likely outcome for ParameterP = 0.7 and NumberFlips = 8?

The most likely outcome is 6.

"""
