__author__ = "Derek Heidtke"
__NetID__ = "derek.heidtke"
__GitHubID__ = "derekheidtke"
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

# Define the biased coin-flip function:
# Returns ONE with probability, p; and ZERO with probability, (1-p).
def biasedcoinflip(p=0.5):
    if ( random.random() <  p):
    	return 1
    else:
    	return 0

# ================================================================================
# ================================================================================
# First part of simulation:
# Verify that as NumberTrials increases, experimental P(flipping a ONE)
# 	approaches ParameterP.

ParameterP = 0.7
NumberFlips = 8
NumberTrials = 100000
Trials = []				# records results of NumberTrials trials

# Loop that flips the coin many times
for i in range(0, NumberTrials):
    Trials.append(biasedcoinflip(ParameterP))

TrialAverage = sum(Trials) / (1.0 * len(Trials))
print 'The average number of ones is {0:.4f}.'.format(TrialAverage)

# ================================================================================
# Second part of simulation:
# Observe how many ONEs occur out of a set number of flips (NumberFlips).
# Repeat experiment many times.

SumTrials = []

# Sums NumberFlips outcomes of biasedcoinflip() and appends the result to list SumTrials
for i in range(0, NumberTrials):
	tmpSum = 0
	for j in range(0,NumberFlips):
		tmpSum += biasedcoinflip(ParameterP)
	SumTrials.append(tmpSum)

Distribution = []
for i in range(0, NumberFlips + 1):
    Distribution.append(SumTrials.count(i) / (1.0 * NumberTrials))

# Sum the values of all the elements contained in list Distribution and print the result.
print repr(sum(Distribution))  # should be equal to 1.0

# ================================================================================
# Plot formatting
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

# ================================================================================
# ================================================================================

"""
Describe what happens to the figure as you vary ParameterP from zero to one.

	- As ParameterP increases, the figure shifts more and more to the right.
	i.e., The height of the bars represent how likely it is to have X number
	of successful (coin-flip results in a ONE) flips out of eight. So, as
	the probability of flipping a ONE increases, it is more likely that all
	of the coin flips result in ONE.


What is the most likely outcome for ParameterP = 0.7 and NumberFlips = 8?

	- The experimenter is most likely to see 6 ONEs out of the eight biased
	coin-flips, with a probability of approximately 30%.

"""
