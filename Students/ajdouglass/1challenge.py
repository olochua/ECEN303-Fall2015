__author__ = "Andrew Douglass"
__NetID__ = "adoulgas"
__GitHubID__ = "ajdouglass"
__challenge__ = "1"
__version__ = "1.0"
__grader__ = ""
__SelfGrade__ = "5pt"
__PeerGrade__ = ""

"""
Random Signals and Systems
Course: ECEN 303-502
Maximum Grade: 5pt
"""

import random
import math
import matplotlib.pyplot as plt


ParameterP = 0.7           # odds of getting a 1 on the coin flip
NumberFlips = 8            # number of coin clips
NumberTrials = 100000      # total test cases
Trials = []                # list to hold odds of each sum


"""returns 1 for heads and 0 for tails, p denotes
the odds that 1 will be returned """
def biasedcoinflip(p=0.5):       # define method, give default value to p
    if random.random() < (1-p):  # generate random number between 0 and 1, if it is less than 1-p, return 0
        return 0
    else:                        # otherwise return 1
        return 1


for TrialIndex1 in range(0, NumberTrials):      # run for loop from 0 to NumberTrials, assign each int to TrialIndex1
    Trials.append(biasedcoinflip(ParameterP))   # add coin flip to end of Trials list

TrialAverage = sum(Trials) / (1.0 * len(Trials))      # find the average number of 1's in Trials list
print('The average number of ones is {0:.4f}.'.format(TrialAverage))  # print this average

SumTrials = []          # create empty list named SumTrials

for TrialIndex2 in range(0, NumberTrials):      # define for loop that runs from 0 to NumberTrials
    sum = 0                                     # initialize variable sum to 0
    for item in range(0,NumberFlips):           # define for loop that runs from 0 to NumberFlips
        sum = sum + biasedcoinflip(ParameterP)  # add another biasedcoinflip toss to sum
    SumTrials.append(sum)                       # add this sum to the end of the SumTrials list

Distribution = []       # create empty list named Distribution
for OutcomeIndex1 in range(0, NumberFlips + 1):         # for loop from 0 to 1 plus the NumberFlips
    Distribution.append(SumTrials.count(OutcomeIndex1) / (1.0 * NumberTrials))

print(repr(Distribution))       # display the value distribution
sum = 0                         # set variable sum to 0
for item in Distribution:       # iterate over Distribution list by assigning each element to item
    sum = sum + item            # add each item in Distribution to the sum
print(sum)                      # print this sum (should be equal to 1)

OutcomeIndex2 = range(0, NumberFlips + 1)          # set range of values from 0 to 1 plus NumberFlips
num_bins = len(OutcomeIndex2)                      # get length of this range
bar_width = 0.8                                    # set width of bars in bar graph
XticksIndex = [(outcome + (0.5 * bar_width)) for outcome in OutcomeIndex2]      # set ticks on x-axis
opacity = 0.4                                      # make slightly transparent

plt.bar(OutcomeIndex2, Distribution, bar_width, alpha=opacity, color='b')  # create bars in graph
plt.xlabel("Value")                 # label x-axis
plt.ylabel("Probability")           # label y-axis
plt.xticks(XticksIndex, OutcomeIndex2)          # plot the x-axis tick marks
plt.show()                          # display the graph

"""
Describe what happens to the figure as you vary ParameterP from zero to one.
As the ParameterP varies from 0 to 1, the bar graph shifts from becoming most probable near zero,
to becoming most probable near 8. As ParameterP gets close to 1, there is a higher probability that
the coin flip will result in a 1. With a higher probability, the odds of receiving a higher sum on 8
flips increases. The opposite happens as the ParameterP gets close to 0. In this situation, the chances
of flipping a 0 increase which causes the values of the sum to be relatively low.

What is the most likely outcome for ParameterP = 0.7 and NumberFlips = 8?
The most likely outcome with the given parameters above is 6. The value 6 had an approximate
probability of 0.29697. This was then followed by 5 which had a probability of 0.25382. This is
an accurate result since the probability of rolling a 1 is 70% where the highest value possible is 8.
Therefore 70% of 8 is 5.6 which is a good estimate of the actual result of 6.

"""
