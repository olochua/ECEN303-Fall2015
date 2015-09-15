__author__ = "Philip Bowie"
__NetID__ = "bowiepj"
__GitHubID__ = "bowiepj"
__challenge__ = "1"
__version__ = "3.4"
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
    if random.random()<p:
        return 1
        #return 1 if probability is p
    else:
        return 0
        #return 0 if probability is 1-p


for TrialIndex1 in range(0, NumberTrials):  #run the tests for all the trials
    Trials.append(biasedcoinflip(ParameterP)) #and append the results

TrialAverage = sum(Trials) / (1.0 * len(Trials))
#Average to check, should be close to ParameterP
print ('The average number of ones is {0:.4f}.'.format(TrialAverage))

SumTrials = []
Temp = 0
#make variable to add tests to sum
for attempt in range(0, NumberTrials):
    for TrialIndex2 in range(0, NumberFlips):
        Temp = Temp + biasedcoinflip(ParameterP) #sum up a single test
    SumTrials.append(Temp)  #add the sum of a single test to the other tests
    Temp = 0    #reset the variable to use again for the next test

Distribution = []
for OutcomeIndex1 in range(0, NumberFlips + 1):
    Distribution.append(SumTrials.count(OutcomeIndex1) / (1.0 * NumberTrials))

print (repr(Distribution))
print (sum(Distribution)) #print the sum of elements in Distribution, should be 1

#Designing the graph
OutcomeIndex2 = range(0, NumberFlips + 1)
num_bins = len(OutcomeIndex2)
bar_width = 0.8
XticksIndex = [(outcome + (0.5 * bar_width)) for outcome in OutcomeIndex2]
opacity = 0.4

#plotting the graph with labels on the axis
plt.bar(OutcomeIndex2, Distribution, bar_width, alpha=opacity, color='b')
plt.xlabel("Value")
plt.ylabel("Probability")
plt.xticks(XticksIndex, OutcomeIndex2)
plt.show()

"""
Describe what happens to the figure as you vary ParameterP from zero to one.
As the ParameterP moves from zero to one, the graph shifts over in columns showing a higher
chance of getting 1 compared to a 0. When ParameterP is on the ends so if it's at 0,
then the columns is solely over 0 and if it's 1 then it's solely over 1 because
there isn't a possibility of the other.

What is the most likely outcome for ParameterP = 0.7 and NumberFlips = 8?
At a ParameterP of .7 you would find 6 to be the most likely outcome when there are
8 flips. With a probability of .3.

"""
