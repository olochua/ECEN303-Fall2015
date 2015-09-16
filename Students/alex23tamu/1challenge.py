__author__ = "Alejandro Penaloza Rodriguez"
__NetID__ = "alex23"
__GitHubID__ = "alex23tamu"
__challenge__ = "1"
__version__ = "0.0"
__grader__ = ""
__SelfGrade__ = "3"
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


      if random.random() <= 0.5:
        Trials.append(1) #Probability of Heads 0.5, Heads = 1 (True)

    else:
        Trials.append(0) #Probability of Tails 0.5, Tails = 0 (False)


for TrialIndex1 in range(0, NumberTrials):
    Trials.append(biasedcoinflip(ParameterP))



TrialAverage = sum(Trials) / (1.0 * len(Trials))
print 'The average number of ones is {0:.4f}.'.format(TrialAverage)

SumTrials = []

for TrialIndex2 in range(0, NumberTrials):
 
cflips = []
    for TrialIndex3 in range(0, NumberFlips):
        cflips.append(biasedcoinflip(ParameterP))
    SumTrials.append(sum(countflips))


Distribution = []
for OutcomeIndex1 in range(0, NumberFlips + 1):
    Distribution.append(SumTrials.count(OutcomeIndex1) / (1.0 * NumberTrials))

print repr(Distribution)


print sum(Distribution)

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
As ParameterP varies from zero to one the outcome is a low number when ParameterP is close
to zero, and changes to high numbers as ParameterP tends to one.

What is the most likely outcome for ParameterP = 0.7 and NumberFlips = 8?
Six would be the most likely outcome for these circumstances.
"""
