__author__ = "Morgan Frakes"  # EDIT
__NetID__ = "mgfrakes13"  # EDIT
__GitHubID__ = "mgfrakes"  # EDIT
__SelfGrade__ = ""  # EDIT
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
    for BinomialIndex in range(0, n):
        numberones += biasedcoinflip(p)
    return numberones


def poisson(parameterpoisson=10):

    finish = random.random()
    k = 0
    pmf = 0
    while (pmf < finish):
        pmf += (pow(parameterpoisson, k) * math.exp(-1*parameterpoisson)) / math.factorial(k)
        k += 1

    return k - 1


def experiment3(parameterpoisson3=10, p=0.5):
    return binomialflips(poisson(parameterpoisson3), p)
    # return poisson(binomialflips(parameterpoisson3, p))


ParameterPoisson = 10
NumberTrials = 100000
TrialSequence = []

for TrialIndex1 in range(0, NumberTrials):
    TrialSequence.append(experiment3(ParameterPoisson))
print sum(TrialSequence)/len(TrialSequence)

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
# Answer 1: 5

# Question 2: What is the type of experiment3()?
# Answer 2: Poisson

# Question 3: Do the two distributions match?
# Answer 3: They are similar, but don't match completely.

