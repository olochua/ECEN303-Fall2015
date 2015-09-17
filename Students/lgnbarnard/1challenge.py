__author__ = "Logan Barnard"
__NetID__ = "lgn_barnard"
__GitHubID__ = "lgnbarnard"
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


ParameterP = 0.7          #chance to get a 1 per coin flip
NumberFlips = 8           #coin flips per trial
NumberTrials = 100000     #total trials
Trials = []



def biasedcoinflip(p=0.5):
    if (random.random()<p): #if the random number generated is < p, return a 1 for heads
        return 1
    else:                    #otherwise return a 0 for tails
        return 0



for TrialIndex1 in range(0, NumberTrials):
    Trials.append(biasedcoinflip(ParameterP))

TrialAverage = sum(Trials) / (1.0 * len(Trials))                        #average number of 1s in trials
print 'The average number of ones is {0:.4f}.'.format(TrialAverage)     #print out average

SumTrials = []

for TrialIndex2 in range(0, NumberTrials):
    totalflips = 0

    for TrialIndex3 in range(0, NumberTrials):     #adds up total outcomes of the biasedcoinflip and appends to SumTrials
        totalflips += biasedcoinflip(ParameterP)

    SumTrials.append(totalflips)


Distribution = []
for OutcomeIndex1 in range(0, NumberFlips + 1):
    Distribution.append(SumTrials.count(OutcomeIndex1) / (1.0 * NumberTrials))

print repr(Distribution)
Sum = 0
for OutcomeIndex3 in range(0, NumberFlips + 1):   #adds up all elements in distribution and prints the sum
    Sum += Distribution[OutcomeIndex3]
print(Sum)

OutcomeIndex2 = range(0, NumberFlips + 1)
num_bins = len(OutcomeIndex2)
bar_width = 0.8
XticksIndex = [(outcome + (0.5 * bar_width)) for outcome in OutcomeIndex2]
opacity = 0.4

plt.bar(OutcomeIndex2, Distribution, bar_width, alpha=opacity, color='b')      #create graph
plt.xlabel("Value")
plt.ylabel("Probability")
plt.xticks(XticksIndex, OutcomeIndex2)
plt.show()

"""
Describe what happens to the figure as you vary ParameterP from zero to one.

As ParameterP increases, the chance that each coin flip in each trial will be 1 also increases. So a 0 ParameterP
would end in all 0s, or all tails, while a 1 ParameterP would end in all 1s or heads.

What is the most likely outcome for ParameterP = 0.7 and NumberFlips = 8?

The most likely outcome would be 6. 6 is most likely due to  each flip in the trial having a .7 chance to be 1, and
there are 8 flips total, averaging to be about 5.6.
"""
