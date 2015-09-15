__author__ = "Charles Wallace"
__NetID__ = "chaswallace3"
__GitHubID__ = "chaswallace3"
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


ParameterP = 0.7
NumberFlips = 8
NumberTrials = 100000
Trials = []

#Biased coin flip function, returns one with
# desired probability, 0 otherwise
def biasedcoinflip(p=0.5):
    if(random.random()<=p):
        return 1
    else:
        return 0

#Appends the results of biasedcoinflip to the list: "Trials"
for TrialIndex1 in range(0, NumberTrials):
    Trials.append(biasedcoinflip(ParameterP))

#Finds the overall average number of ones
TrialAverage = sum(Trials) / (1.0 * len(Trials))
print ("The average number of ones is %.4f" % TrialAverage)


SumTrials = []

#This section works to add the results of a trial where a coin is
#flipped NumberFlips times for NumberTrials amount of trials
for TrialIndex2 in range(0, NumberTrials):
    Sum = 0

    for flips in range(0, NumberFlips):
        Sum = Sum + biasedcoinflip(ParameterP)
    SumTrials.append(Sum)

#This calculates the probability of each value of SumTrials
#from 0 to Numberflips+1 appearing for every coin flip
Distribution = []
for OutcomeIndex1 in range(0, NumberFlips + 1):
    Distribution.append(SumTrials.count(OutcomeIndex1) / (1.0 * NumberTrials))

print repr(Distribution)
print (sum(Distribution))


#This is responsible for plotting Distribution on a graph
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

As ParameterP is varied from zero to one, the average value of the distribution
changes. This changes the center of the distribution curve to be centered over
the most probable outcome.


What is the most likely outcome for ParameterP = 0.7 and NumberFlips = 8?

The most likely outcome given the above parameters is 6
"""
