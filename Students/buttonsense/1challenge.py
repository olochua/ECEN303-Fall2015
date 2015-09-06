__author__ = "Seungwon Yoon"
__NetID__ = "ysw0927"
__GitHubID__ = "buttonsense"
__challenge__ = "1"
__version__ = "3.4"
__grader__ = ""
__SelfGrade__ = ""
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

#biasedcoinflip that returns 1 or 0
def biasedcoinflip(p=0.5):
    if random.random() < p:
        return 1
    else:
        return 0


for TrialIndex1 in range(0, NumberTrials):
    Trials.append(biasedcoinflip(ParameterP))

TrialAverage = sum(Trials) / (1.0 * len(Trials))
print('The average number of ones is {0:.4f}.'.format(TrialAverage))

SumTrials = []

SumTrials = (list(sum(Trials[x:x+NumberFlips]) for x in range(0,len(Trials), NumberFlips)))
#sums NumberFlips outcomes from list Trials and appends the result to list Sumtrials
#I had no idea how to do this using your for loops

Distribution = []
for OutcomeIndex1 in range(0, NumberFlips + 1):
    Distribution.append(SumTrials.count(OutcomeIndex1) / (1.0 * NumberTrials))


print(repr(Distribution))
print(sum(Distribution)) #print the sum of elements in Distribution

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
Probability of getting 1(Head) gets bigger as we change ParameterP from zero to one.

What is the most likely outcome for ParameterP = 0.7 and NumberFlips = 8?
Average number of ones will be close to 0.7 and distribution will show higher values.


"""
