__author__ = "Bailey Barksdale"
__NetID__ = "bailey13"
__GitHubID__ = "bkb0917"
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
#import matplotlib.pyplot as plt


ParameterP = 0.3
NumberFlips = 8
NumberTrials = 100000
Trials = []


def biasedcoinflip(p=0.5):
    prob = random.randrange(100)/100
    if prob < p:
        return 1
    else:
        return 0


for TrialIndex1 in range(0, NumberTrials):
    Trials.append(biasedcoinflip(ParameterP))

TrialAverage = sum(Trials) / (1.0 * len(Trials))
print('The average number of ones is {0:.4f}.'.format(TrialAverage))

SumTrials = []
CurrentSum = 0
for TrialIndex2 in range(0, NumberTrials):
    CurrentSum = 0
    for NumFlips in range(0, NumberFlips):
        CurrentFlip = biasedcoinflip(ParameterP)
        CurrentSum += CurrentFlip
    SumTrials.append(CurrentSum)


Distribution = []
for OutcomeIndex1 in range(0, NumberFlips + 1):
    Distribution.append(SumTrials.count(OutcomeIndex1) / (1.0 * NumberTrials))


print(repr(Distribution))
DistSum = 0;
for OutcomeIndex3 in range(0, NumberFlips+1):
    DistSum += Distribution[OutcomeIndex3]
print(DistSum)

"""
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
"""
Describe what happens to the figure as you vary ParameterP from zero to one.

As you vary ParameterP from 0 to 1, the biasedcoinflip() goes from outputing
more 0s than 1s (a bias towards 0) to a fairly even amount of 0s and 1s to more
1s than 0s (a bias towards 1). The figure shows a bar graph that is skewed based
on ParameterP where the probability of getting a 1 for 0,1,2,3...8 flips is the
height of the bar. When ParameterP is closer to 0, the graph is skewed to the right
or the probabilities of getting a 1 on only a few of the 8 flips are higher than
getting a 1 on more of the flips. When ParameterP is close or equal to 0.5, the
graph is balanced where the probabilities of getting a 1 on about half of the flips
are higher than on more or less of the flips. When ParameterP is closer to 1, the
graph is skewed to the left or the probabilities of getting a 1 on more of the 8
flips are higher than on less of the flips.


What is the most likely outcome for ParameterP = 0.7 and NumberFlips = 8?

If 0.7 is the probability bias and there are 8 flips, then in theory about
5.6 flips would be getting a 1 for 70% of the time in 8 flips. Since one cannot
have part of a flip, the most likely outcome for )arameterP = 0.7 and
NumberFlips = 8, is 6 flips.

"""
