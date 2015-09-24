__author__ = "Joshua Ruff"
__NetID__ = "joshruff"
__GitHubID__ = "joshruff"
__challenge__ = "1"
__version__ = "0.1"
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




def biasedcoinflip(p=0.5):
    # Returns 1 for Heads, 0 for tails
	result=random.random()*1000
	return int(result>=(1-p)*1000)


for TrialIndex1 in range(0, NumberTrials):
	heads=0
	for flipIndex in range(0, NumberFlips+1):
		heads=heads+biasedcoinflip(ParameterP)
	Trials.append(heads)

TrialAverage = sum(Trials) / (1.0 * len(Trials))
#print ("The average number of ones is {0:.4f}.").format(TrialAverage)
print(TrialAverage)

SumTrials = [0]*(NumberFlips+1)
for TrialIndex2 in range(0, NumberTrials):
	SumTrials[Trials[TrialIndex2]-1]+=1  
print(SumTrials)
    # Add NumberFlips coin flips for each SumTrials outcome
    #

Distribution = []
for OutcomeIndex1 in range(0, NumberFlips+1):
    Distribution.append(SumTrials[OutcomeIndex1] / (1.0 * NumberTrials))

print(repr(Distribution))
# EDIT
# Print the sum of the elements in Distribution


OutcomeIndex2 = range(0, NumberFlips +1)
num_bins = len(OutcomeIndex2)
bar_width = 0.8
XticksIndex = [(outcome + (0.5 * bar_width)) for outcome in OutcomeIndex2]
opacity = 0.4

plt.bar(OutcomeIndex2, Distribution, bar_width, alpha=opacity, color='b')
plt.xlabel("Value")
plt.ylabel("Probability")
plt.xticks(XticksIndex, OutcomeIndex2)


#"""
#Describe what happens to the figure as you vary ParameterP from zero to one.
print('The distribution shifts from the left to the right as ParameterP increases from \nzero to one.')

#What is the most likely outcome for ParameterP = 0.7 and NumberFlips = 8?
print('The most likely outcome is a result of 5 heads given 8 trials and p(h)=.7\n5 and 6 are nearly equally likely based on the trials.')
plt.show()
#"""
