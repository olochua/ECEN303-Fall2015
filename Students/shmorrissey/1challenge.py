__author__ = "Shannon Morrissey"
__NetID__ = "shannon.morrissey"
__GitHubID__ = "shmorrissey"
__challenge__ = "1"
__version__ = "0.0"
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


def biasedcoinflip(p=0.5):  #creation of coin flip method
    if random.random() < p:
        return 1
    else:
        return 0



for TrialIndex1 in range(0, NumberTrials):
    Trials.append(biasedcoinflip(ParameterP))

TrialAverage = sum(Trials) / (1.0 * len(Trials))
print 'The average number of ones is {0:.4f}.'.format(TrialAverage)

SumTrials = []

for TrialIndex2 in range(0, NumberTrials):
    sum = 0
    for flip in range(0, NumberFlips):
        sum += biasedcoinflip(ParameterP)   #sum is the number of times you get a 1
    SumTrials.append(sum)

Distribution = []
for OutcomeIndex1 in range(0, NumberFlips + 1):
    Distribution.append(SumTrials.count(OutcomeIndex1) / (1.0 * NumberTrials))

print repr(Distribution)

dist = 0
for item in range(0, len(Distribution)):
    dist += Distribution[item]  #prints the elements in Distribution
print "The Sum of the Distribution is " + str(dist)

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
As we vary Parameter P from 0 to 1, the distribution adjusts to the new probability only along the x-axis. When P is 0, 
there is no chance to get smaller than that, as we cannot get negative probabilities, so the probability is 0.
When P is 1, we cannot get a probability more than, 1 so the probability is 1. The most balanced and equally distributed graph
would be P=0.5. The distributions in between 0 and 1 varies evenly across the graph.
What is the most likely outcome for Parameter P = 0.7 and NumberFlips = 8?
The most likely outcome was 6 and its probability was close to .3.
"""
