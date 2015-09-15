__author__ = "Rodney Siders"
__NetID__ = "rodney6359"
__GitHubID__ = "rodney6359"
__challenge__ = "1"
__version__ = "1.0"
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

#Makes sure we have a mixed up coin to prevent puesdo random
def biasedcoinflip(prob=0.5):
   for g in range(0,1000):
    if (random.random() >= prob):
        return 1
    else:
        return 0

for TrialIndex1 in range(0, NumberTrials):
    Trials.append(biasedcoinflip(ParameterP))

TrialAverage = sum(Trials) / (1.0 * len(Trials))
print 'The average number of ones is {0:.4f}.'.format(TrialAverage)

SumTrials = []

# So this works to make the results of the baisedcoinflip set to a variable(junk)
# and from there sums it up and place it in SumTrials
for TrialIndex2 in range(0, NumberTrials):

    junk = 0
    for flips in range(0, NumberFlips):
        junk += biasedcoinflip(ParameterP)
        SumTrials.append(junk)

Distribution = []
for OutcomeIndex1 in range(0, NumberFlips + 1):
    Distribution.append(SumTrials.count(OutcomeIndex1) / (1.0 * NumberTrials))

print repr(Distribution)
# Print the sum of the elements in Distribution
print (sum(Distribution))

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
With ParameterP increasing from 0 to 1 the figure shifts to the right,
 with the center of the distribution moving across the x-axis 

What is the most likely outcome for ParameterP = 0.7 and NumberFlips = 8?
Given the parameter, it would be 6.
"""
