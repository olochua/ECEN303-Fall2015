__author__ = "Matthew Grogan"
__NetID__ = "grogan2122"
__GitHubID__ = "mdgrogan"
__challenge__ = "1"
__version__ = "1"
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
    return 1 if random.random()<p else 0


for TrialIndex1 in range(0, NumberTrials):
    Trials.append(biasedcoinflip(ParameterP))

TrialAverage = sum(Trials) / (1.0 * len(Trials))
print 'The average number of ones is {0:.4f}.'.format(TrialAverage)

SumTrials = []

for TrialIndex2 in range(0, NumberTrials):
	sumNumberFlips = []
	for TrialIndex3 in range(0, NumberFlips):
		sumNumberFlips.append(biasedcoinflip(ParameterP))
	SumTrials.append(sum(sumNumberFlips))

Distribution = []
for OutcomeIndex1 in range(0, NumberFlips + 1):
    Distribution.append(SumTrials.count(OutcomeIndex1) / (1.0 * NumberTrials))

print repr(Distribution)
print 'The sum of the distribution is {0:.4f}.'.format(sum(Distribution))

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

As ParameterP is increased from zero to one, the figure is shifted to the right
with the peak of the distribution roughly following ParameterP

What is the most likely outcome for ParameterP = 0.7 and NumberFlips = 8?

The most likely outcome is that of a 6.

"""
