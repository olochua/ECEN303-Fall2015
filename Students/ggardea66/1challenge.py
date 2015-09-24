__author__ = "Gissel Gardea"
__NetID__ = "gardegi059"
__GitHubID__ = "ggardea66"
__challenge__ = "1"
__version__ = "3.5.0"
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


ParameterP = 0.7
NumberFlips = 8
NumberTrials = 100000
Trials = []


def biasedcoinflip(p=0.5): #Method for biased coin flip
    if random.random() < p:
        return 1 #coin is heads
    else:
        return 0 #coin is tails

for TrialIndex1 in range(0, NumberTrials):
    Trials.append(biasedcoinflip(ParameterP))

TrialAverage = sum(Trials) / (1.0 * len(Trials))
print 'The average number of ones is {0:.4f}.'.format(TrialAverage)

SumTrials = []

for TrialIndex2 in range(0, NumberTrials):
    addNumberFlips = 0 #start of with 0, indicating there are no flips 
for index in range(0,NumberFlips): #the number of flips ranges from 0 to 8
    addNumberFlips += biasedcoinflip(ParameterP) 
SumTrials.append(addNumberFlips)#adds NumberFlips for each SumTrial

Distribution = []
for OutcomeIndex1 in range(0, NumberFlips + 1):
    Distribution.append(SumTrials.count(OutcomeIndex1) / (1.0 * NumberTrials))

print repr(Distribution) #prints the sum of the elements in Distribution
add_Distrib = 0
for item in Distribution:
    add_Distrib += item
print(repr(add_Distrib))

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

The graph shifts from left to right. This is because the probability of landing on a one increases as you increase flips. 
When the ParameterP is equal to zero, the graph shows the value of x is 0. This shows that there is no probability of 
receiving a one. This is because there are no flips as this point, once you increase the number of flips, the probability of 
receiving a one also increases. When ParameterP increases there are more possibilities of landing on a number greater than one. 
The larger the x values are, the less probability there are for the smaller x values. When ParameterP is 1, the graph is a single bar 
on the 8 x value. This shows that all the flips returned a 1. The probability of receiving a one is 1 or 100% and the graph proves
that.

What is the most likely outcome for ParameterP = 0.7 and NumberFlips = 8?

When ParameterP = .7 and the NumberFlips = 8, the outcome of it being 6 is roughly 29.8% or if you round
up, 30%.

"""
