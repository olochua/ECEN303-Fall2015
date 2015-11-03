__author__ = "Andrew Douglass"
__NetID__ = "adoulgas"
__GitHubID__ = "ajdouglass"
__SelfGrade__ = "5pt"
__Challenge__ = "3"

"""
Random Signals and Systems
Course: ECEN 303-502
Maximum Grade: 5
"""


import random                      # obtain a random number
import math                        # use e constant
import matplotlib.pyplot as plt    # plot poisson distribution


def biasedcoinflip(p=0.5):
    """
    This method returns a one with probability p and it returns a zero with
    probability (1 - p). The default parameter is p=0.5; this can be changed
    by passing an argument to the method.
    """
    return math.floor(random.random() + p)


def binomialflips(n=1, p=0.5):
    """
    This method returns a binomial random variable with parameters n and p.
    The default parameters are n=1 and p=0.5; this can be changed by passing
    arguments to the method.
    """
    numberones = 0
    for BinomialIndex in range(0,n):
        numberones += biasedcoinflip(p)
    return numberones


def poisson(parameterpoisson=10):
    """
    This method calculates and returns the value of a poisson random variable
    with the value for lambda as that passed in the parameterpoisson parameter
    """
    k = 0                  # start k at 0
    p = random.random()    # generate a random number between 0 and 1.0
    el = math.exp(-1 * parameterpoisson)    # e^-lambda
    while p > el:    # while the random generated number is greater than e^-lambda
        k = k + 1    # increment k
        p = p * random.random()    # multiply p by new random number between 0 and 1.0
    return k                       # return this value for k


def experiment3(parameterpoisson3=10, p=0.5):
    return binomialflips(poisson(parameterpoisson3), p)
    # return poisson(binomialflips(parameterpoisson3, p))


ParameterPoisson = 10     # parameter for poisson random variable
NumberTrials = 100000     # number of trails to perform
TrialSequence = []        # store values of each experiment

for TrialIndex1 in range(0, NumberTrials):      # execute NumberTrails times
    TrialSequence.append(experiment3(ParameterPoisson))    # add return value of experiment
print(sum(TrialSequence)/len(TrialSequence))     # print the mean of experiment3

Distribution = []      # hold the distribution of the experiment
for OutcomeIndex1 in range(0, 21):    # run 21 times
    Distribution.append(TrialSequence.count(OutcomeIndex1) / (1.0 * NumberTrials))  # count distribution percentage

OutcomeIndex2 = range(0, 21)    # run 21 times
num_bins = len(OutcomeIndex2)   # hold the number of distributions to graph
bar_width = 0.8                 # width of each bar graph
XticksIndex = [(outcome + (0.5 * bar_width)) for outcome in OutcomeIndex2]  # spacing of each bar graph
opacity = 0.4      # transparency of graph

plt.bar(OutcomeIndex2, Distribution, bar_width, alpha=opacity, color='b')   # plot the bar graph
plt.xlabel("Value")                 # label the x axis
plt.ylabel("Probability")           # label the y axis
plt.xticks(XticksIndex, OutcomeIndex2)     # space out each bar for each distribution
plt.show()                          # show the graph

# Question 1: What is the mean of experiment3()?
# The mean is approximately 5 (plus or minus 0.01)

# Question 2: What is the type of experiment3()?
# experiment3 resembles a Poisson random variable as the
# number of trails increases

# Question 3: Do the two distributions match?
# No, distributions are different despite equivalent means
