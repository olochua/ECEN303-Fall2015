__author__ = "Jui Yen Chua"
__NetID__ = "olochua"
__GitHubID__ = "olochua"
__challenge__ = "1"
__version__ = "0.0"
__grader__ = "Weston Torti"
__SelfGrade__ = "5"
__PeerGrade__ = "5"

"""
Random Signals and Systems
Course: ECEN 303-502
Maximum Grade: 5pt
"""

import random
import math
import matplotlib.pyplot as plt

#defining the variables
ParameterP = 0.7
NumberFlips = 8
NumberTrials = 100000

#this stores the sum of outcome each coin flip test
temp_val = 0

#this stores the total of individual probability
total = 0

#function returns a 1 using the probability p, 
#and returns a 0 with the probability 1-p
def biasedcoinflip(p=0.5):
    if random.random()<p:
        return 1
    else:
        return 0

#compute NumberTrials of tests and append the result to Trials.
Trials = []

for TrialIndex1 in range(0, NumberTrials):
    Trials.append(biasedcoinflip(ParameterP))

#The average (which should be very close to the value of ParameterP) of Trials
TrialAverage = sum(Trials) / (1.0 * len(Trials))
print 'The average number of ones is {0:.4f}.'.format(TrialAverage)

#compute NumberTrials of NumberFlips-times of coin flip and append the result to SumTrials
SumTrials = []

for attempt in range(0,NumberTrials):
    for TrialIndex2 in range(0, NumberFlips):
        #sums up the coin flips in a test
        temp_val = temp_val + biasedcoinflip(ParameterP)  
    
    SumTrials.append(temp_val)
    #after appending the result, reset the variable
    temp_val = 0

#compute the distribution of the outcome
Distribution = []
for OutcomeIndex1 in range(0, NumberFlips + 1):
    Distribution.append(SumTrials.count(OutcomeIndex1) / (1.0 * NumberTrials))

print repr(Distribution)

#sums up individual probability (which should return a 1 since the probabilities are not overlapping)
for value in Distribution:
    total = total + value

print "The sum of elements in Distribution is: " + str(total)

#setting up the values to plot the graph
OutcomeIndex2 = range(0, NumberFlips + 1)
num_bins = len(OutcomeIndex2)
bar_width = 0.8
XticksIndex = [(outcome + (0.5 * bar_width)) for outcome in OutcomeIndex2]
opacity = 0.4

#plotting the graph with necessary labels
plt.bar(OutcomeIndex2, Distribution, bar_width, alpha=opacity, color='b')
plt.xlabel("Value")
plt.ylabel("Probability")
plt.xticks(XticksIndex, OutcomeIndex2)
plt.show()


"""
Describe what happens to the figure as you vary ParameterP from zero to one.
As ParameterP increases from 0 to 1, the center of the series of bar graph - where the peak is located - shifts from left to right in the figure.
As for the remaining bar graphs on both sides of the peak, they gradually decrease towards the edges. In other words, it appears to be a shift in the 
bell graph.

What is the most likely outcome for ParameterP = 0.7 and NumberFlips = 8?
The most likely outcome happens in value = 6, with a probability of 0.3.

"""
