__author__ = "Alexander Garcia"
__NetID__ = "alexgarcia2013"
__GitHubID__ = "alexgarcia2013"
__challenge__ = "1"
__version__ = "0.0"
__grader__ = "Zachary Smadi"
__SelfGrade__ = "0"
__PeerGrade__ = ""

"""
Random Signals and Systems
Course: ECEN 303-502
Maximum Grade: 5pt
"""

import random
import math
#import matplotlib.pyplot


ParameterP = 0.3
NumberFlips = 8
NumberTrials = 100000

Trials = []
def biasedcoinflip(p=0.5):

    for TrialIndex1 in range(0, NumberTrials):
        Trials.append(biasedcoinflip(ParameterP))
        # corresponding 1 to p
        if random.random() < p:
            biasedcoinflip().append(1)

        else:
             biasedcoinflip().append(0)


#TrialAverage = sum(Trials) / (1.0 * len(Trials))
print('The average number of ones is {0:.4f}.'.format(sum(Trials)))

SumTrials = []

for TrialIndex2 in range(0, NumberTrials):

    Distribution = []

for OutcomeIndex1 in range(0, NumberFlips + 1):
    Distribution.append(SumTrials.count(OutcomeIndex1) / (1.0 * NumberTrials))

print(repr(Distribution))
# EDIT
# Print the sum of the elements in Distribution
#

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
