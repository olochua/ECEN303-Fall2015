__author__ = "Madeline Kinnaird"
__NetID__ = "mrk13"
__GitHubID__ = "mkinnaird16"
__challenge__ = "1"
__version__ = "1.4"
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
    if random.randon() < p:
        return 1
    else:
        return 0

for TrialIndex1 in range(0, NumberTrials):
    Trials.append(biasedcoinflip(ParameterP))

TrialAverage = sum(Trials) / (1.0 * len(Trials))
print 'The average number of ones is {0:.4f}.'.format(TrialAverage)

SumTrials = []

for TrialIndex2 in range(0, NumberTrials):
    flip_sum = 0 #begin with zero as no coins have been flipped
    for index in range (0, NumberFlips): #the range of the number of flips
        flip_sum = += biasedcoinflip(ParameterP)
    SumTrials.append(flip_sum) #this adds flip_sum to SumTrails
        

Distribution = []
for OutcomeIndex1 in range(0, NumberFlips + 1):
    Distribution.append(SumTrials.count(OutcomeIndex1) / (1.0 * NumberTrials))

print repr(Distribution)
distribution_sum = 0 #set distribution sum to 0
for item in Distribution:
    distribution_sum = += item
print(repr(distribution_sum))

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
The figure shows the probability of getting consective flips in a row. As the value on the x axis increases the probability of getting more flips in a row becomes less likely. Varyinig ParameterP is between 1 and 8 flips in a row.

What is the most likely outcome for ParameterP = 0.7 and NumberFlips = 8?
6 flips in a row is the most likely outcome.

"""
