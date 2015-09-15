__author__ = "Jordan Lewallen"
__NetID__ = "jlewallen18"
__GitHubID__ = "jlewallen18"
__challenge__ = "1"
__version__ = "1.0"
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

ParameterP = 0.3
NumberFlips = 8
NumberTrials = 100000
Trials = []


def biasedcoinflip(p=0.5):
    #selects a random value and if it is less than p, then a 1 is returned
    if random.random() < p:
        return 1
    else:
        return 0

for TrialIndex1 in range(0, NumberTrials):
    Trials.append(biasedcoinflip(ParameterP))

TrialAverage = sum(Trials) / (1.0 * len(Trials))
print('The average number of ones is {0:.4f}.'.format(TrialAverage)) #altered from original to work with Python 3.4

SumTrials = []

for TrialIndex2 in range(0, NumberTrials):
    #plugs in the parameterP and computes if it is above or below 0.5
    Temp_Sum = 0
    for add_Number in range(0, NumberFlips):
        Temp_Sum += biasedcoinflip(ParameterP)
    SumTrials.append(Temp_Sum)

Distribution = []
for OutcomeIndex1 in range(0, NumberFlips + 1):
    Distribution.append(SumTrials.count(OutcomeIndex1) / (1.0 * NumberTrials))

print repr(Distribution) 
Sum_Distribution = 0
for disp_elements in Distribution:
    Sum_Distribution += disp_elements
print repr(Sum_Distribution)

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
Describe What happens to the figure as you vary ParameterP from zero to one?
As ParameterP is varied from zero to one, the distrubution probability shifts from left to right as it is becoming more likely that a one will be achieved.
Upon observation, when ParameterP is equal to zero the probability equals zero, which makes logical sense, since there is no chance at obtaining a value of 1.
Then as ParameterP increases, so does the probability of the other values occuring. As the ParameterP grows closer to 1.0, the graph shifts to higher values while 
lower values are displayed less. Finally at ParameterP = 1, the bar is completely in slot 8, simply because all coin flips were a 1.

What is the most likely outcome for ParameterP = 0.7 and NumberFlips = 8?

The most likely value is a 6 with probability of 0.255 or 26%

""" 
