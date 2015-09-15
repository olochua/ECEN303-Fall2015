__author__ = "Fletcher Watts"
__NetID__ = "augustus1994"
__GitHubID__ = "augusus1994"
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


ParameterP = .7
NumberFlips = 8
NumberTrials = 100000
Trials = []


def biasedcoinflip(p=0.5):
#create the biasedcoinflip
    if random.random()<p:
		return 1
    else:
		return 0


for TrialIndex1 in range(0, NumberTrials):
    Trials.append(biasedcoinflip(ParameterP))

TrialAverage = sum(Trials) / (1.0 * len(Trials))
print 'The average number of ones is {0:.4f}.'.format(TrialAverage)

SumTrials = []
temp = 0
for TrialIndex2 in range(0, NumberTrials):
    # EDIT
	# store the sum of the biasedcoinflip in temp and then append it to SumTrials
	for TrialIndex2 in range(0,NumberFlips):
		temp = temp + biasedcoinflip(ParameterP)
	#append the sum to SumTrials	
	SumTrials.append(temp)
	#restore temp
	temp = 0

Distribution = []
for OutcomeIndex1 in range(0, NumberFlips + 1):
    Distribution.append(SumTrials.count(OutcomeIndex1) / (1.0 * NumberTrials))

print repr(Distribution)
# EDIT
# Print the sum of the elements in Distribution
for value in Distribution:
    temp = temp + value
print "The sum of the elements in Distribution is " + str(temp)


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
As you vary the figure from zero to one the distribution moves from left to right along the x-axis of the bar graph
It displays the weighted distribution where the peak is 10*ParameterP-1.

What is the most likely outcome for ParameterP = 0.7 and NumberFlips = 8?
The most likely outcome for this was 6 and it had a probability of .3.

"""
