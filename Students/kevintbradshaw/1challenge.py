__author__ = "Kevin Bradshaw"
__NetID__ = "kevintbradshaw"
__GitHubID__ = "kevintbradshaw"
__challenge__ = "1"
__version__ = "0.0"
__grader__ = "Shannon Morrissey"
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
    generated_numbers = random.random()
    if generated_numbers < p:   return 1
    else: return 0


for TrialIndex1 in range(0, NumberTrials):
    Trials.append(biasedcoinflip(ParameterP))

TrialAverage = sum(Trials) / (1.0 * len(Trials))
print 'The average number of ones is {0:.4f}.'.format(TrialAverage)

SumTrials = []

for TrialIndex2 in range(0, NumberTrials):
    sum = biasedcoinflip(ParameterP)
    Trials.append(sum)

Distribution = []
for OutcomeIndex1 in range(0, NumberFlips + 1):
    Distribution.append(SumTrials.count(OutcomeIndex1) / (1.0 * NumberTrials))

print repr(Distribution)
total_elements = 0
for item in Distribution: total_elements = total_elements + item
print(total_elements)

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

As ParameterP is varied from 0 to 1, the distribution varies on the x-axis of the graph towards the right.
This has to do with the increase in probability until it reaches to one (The maximum possible of events in the system).
This distribution is most evenly distributed by setting our Parameter P equal to 0.5.

What is the most likely outcome for ParameterP = 0.7 and NumberFlips = 8?
The most likely outcome is 6 with approximate probability of 0.3.
"""

