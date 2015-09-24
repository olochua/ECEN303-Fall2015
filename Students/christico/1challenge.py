__author__ = "Christian Rodriguez"
__NetID__ = "christico"
__GitHubID__ = "christico"
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


def biasedcoinflip(p=0.5):  #makes biasedcoinflip
    if random.random() < p:
        return 1
    else:
        return 0


for TrialIndex1 in range(0, NumberTrials):
    Trials.append(biasedcoinflip(ParameterP))

TrialAverage = sum(Trials) / (1.0 * len(Trials))
print ('The average number of ones is {0:.4f}.'.format(TrialAverage))

SumTrials = []

for TrialIndex2 in range(0, NumberTrials):
    sum = 0                                     
    for index in range (0, NumberFlips):        
        sum += biasedcoinflip(ParameterP)
    SumTrials.append(sum)
    

Distribution = []
for OutcomeIndex1 in range(0, NumberFlips + 1):
    Distribution.append(SumTrials.count(OutcomeIndex1) / (1.0 * NumberTrials))

print (repr(Distribution))

dist_sum = 0
for item in Distribution:
    dist_sum = dist_sum +item
print(dist_sum)

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

As you vary ParameterP from zero to one the firgure changes along the x-asis for being the most probable to 0 to be near 8. So
 if it gets close to 1, the probabilty is 1. The lower the parameter makes it have a higher probabilty because is there is fewer 
flips. The higher the parameter makes it have a lower probabilty to flipping a 0. 

What is the most likely outcome for ParameterP = 0.7 and NumberFlips = 8?

The most likely outcome is 6

"""
