__author__ = "David Fawcett"  # EDIT
__NetID__ = "dgf378"  # EDIT
__GitHubID__ = "dfawcett"  # EDIT
__SelfGrade__ = "5"  # EDIT
__Challenge__ = "3"

"""
Random Signals and Systems
Course: ECEN 303-502
Maximum Grade: 5
"""


import random
import math
import matplotlib.pyplot as plt

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
    L = math.exp(-parameterpoisson)
    k = 0
    p = 1
    while p > L:
        u = random.random()
        k = k +1
        p = p * u
    return k-1



def plotbinomial(NumberFlips, Bias=0.5):
    NumberTrials = 1000
    ones = []
    for index1 in range(0,NumberTrials):
        ones.append(binomialflips(NumberFlips, Bias))

    probability=[0 for i in range(0,20)]

    for index in range(0,20):
        i = ones.count(index)
        probability[index] = i/NumberTrials

    OutcomeIndex = range(0, 20)
    num_bins = len(OutcomeIndex)
    bar_width = 0.8
    XticksIndex = [(outcome + (0.5 * bar_width)) for outcome in OutcomeIndex]
    opacity = 0.4

    plt.bar(OutcomeIndex, probability, bar_width, alpha=opacity, color='b')
    plt.xlabel("Value")
    plt.ylabel("Probability")
    plt.xticks(XticksIndex, OutcomeIndex)
    plt.show()

def plotpoisson(parameterpoisson,xaxis):
    NumberTrials = 1000
    ones = []
    for index1 in range(0,NumberTrials):
        ones.append(poisson(parameterpoisson))

    probability=[0 for i in range(0,xaxis)]

    for index in range(0,xaxis):
        i = ones.count(index)
        probability[index] = i/NumberTrials

    OutcomeIndex = range(0, xaxis)
    num_bins = len(OutcomeIndex)
    bar_width = 0.8
    XticksIndex = [(outcome + (0.5 * bar_width)) for outcome in OutcomeIndex]
    opacity = 0.4

    plt.bar(OutcomeIndex, probability, bar_width, alpha=opacity, color='b')
    plt.xlabel("Value")
    plt.ylabel("Probability")
    plt.xticks(XticksIndex, OutcomeIndex)
    plt.show()


def plotexperiment3pthenb(parameterpoisson, xaxis=20):
    outcomes = []
    for index in range(0, 1000):
        outcomes.append(experiment3pthenb(parameterpoisson))

    probability=[0 for i in range(0,xaxis)]

    for index in range(0,xaxis):
        i = outcomes.count(index)
        probability[index] = i/1000


    OutcomeIndex = range(0,xaxis)
    num_bins = len(OutcomeIndex)
    bar_width = 0.8
    XticksIndex = [(outcome + (0.5 * bar_width)) for outcome in OutcomeIndex]
    opacity = 0.4

    plt.bar(OutcomeIndex, probability, bar_width, alpha=opacity, color='b')
    plt.title("Poisson of Binomial Random Variable \n lambda = " + repr(parameterpoisson) + " and p = .5")
    plt.xlabel("Value")
    plt.ylabel("Probability")
    plt.xticks(XticksIndex, OutcomeIndex)
    plt.show()

def plotexperiment3bthenp(binomialn, xaxis=20):
    outcomes = []
    for index in range(0, 1000):
        outcomes.append(experiment3bthenp(binomialn))

    probability=[0 for i in range(0,xaxis)]

    for index in range(0,xaxis):
        i = outcomes.count(index)
        probability[index] = i/1000


    OutcomeIndex = range(0,xaxis)
    num_bins = len(OutcomeIndex)
    bar_width = 0.8
    XticksIndex = [(outcome + (0.5 * bar_width)) for outcome in OutcomeIndex]
    opacity = 0.4

    plt.bar(OutcomeIndex, probability, bar_width, alpha=opacity, color='b')
    plt.title("Binomial of Poisson Random Variable \n n = " + repr(binomialn) + " and p = .5")
    plt.xlabel("Value")
    plt.ylabel("Probability")
    plt.xticks(XticksIndex, OutcomeIndex)
    plt.show()

def experiment3(parameterpoisson3=10, p=0.5):
    return binomialflips(poisson(parameterpoisson3), p)
    # return poisson(binomialflips(parameterpoisson3, p))

def experiment3bthenp(parameterpoisson3=10, p=0.5):
    return binomialflips(poisson(parameterpoisson3), p)

def experiment3pthenb(binomialn=10, p=0.5):
    return poisson(binomialflips(binomialn,p))

total = 0
for index in range(0, 1000):
    total += experiment3bthenp()

print("The average is: " + repr(total/1000)+'\n')

print("The following distributions seem the indicate that the distributions of the experiment 3 are poisson. \n")
print("It also does not seem to affect the distribution greatly when the poisson of a binomial random variable is taken \n"
      "as opposed to the binomial of a poisson random variable. The distributions do seem to be more spread out with the \n"
      "poisson of the binomial")


plotexperiment3bthenp(1)
plotexperiment3pthenb(1)
plotexperiment3bthenp(4)
plotexperiment3pthenb(4)
plotexperiment3bthenp(10)
plotexperiment3pthenb(10)
plotexperiment3bthenp(20)
plotexperiment3pthenb(20)





ParameterPoisson = 10
NumberTrials = 100000
TrialSequence = []

for TrialIndex1 in range(0, NumberTrials):
    TrialSequence.append(experiment3(ParameterPoisson))
total = sum(TrialSequence)/len(TrialSequence)
print("The average is: " + repr(total)+ '\n')

Distribution = []
for OutcomeIndex1 in range(0, 21):
    Distribution.append(TrialSequence.count(OutcomeIndex1) / (1.0 * NumberTrials))

OutcomeIndex2 = range(0, 21)
num_bins = len(OutcomeIndex2)
bar_width = 0.8
XticksIndex = [(outcome + (0.5 * bar_width)) for outcome in OutcomeIndex2]
opacity = 0.4

plt.bar(OutcomeIndex2, Distribution, bar_width, alpha=opacity, color='b')
plt.xlabel("Value")
plt.ylabel("Probability")
plt.xticks(XticksIndex, OutcomeIndex2)
plt.show()

# Question 1: What is the mean of experiment3()?
# Answer 1: The mean is 5.

# Question 2: What is the type of experiment3()?
# Answer 2: A poisson random variable.

# Question 3: Do the two distributions match?
# Answer 3: Yes they are very similar and thus can be said to match.
