__author__ = "Alexander Garcia"  # EDIT
__NetID__ = "alexgarcia2013"  # EDIT
__GitHubID__ = "alexgarcia2013"  # EDIT
__SelfGrade__ = "3"  # EDIT
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
    poi= -math.log(1.0 - random.random())/ parameterpoisson
    k = 0
    prob = 1

    while True:
        random.random()
        k = k+1

        prob *= random.random()
        if prob<poi:
            break
    return k

def experiment3(parameterpoisson3=10, p=0.5):
    return binomialflips(poisson(parameterpoisson3), p)
    #return poisson(binomialflips(parameterpoisson3, p))
print(poisson())

ParameterPoisson = 10
NumberTrials = 100000
TrialSequence = []

for TrialIndex1 in range(0, NumberTrials):
    TrialSequence.append(experiment3(ParameterPoisson))
print (sum(TrialSequence)/len(TrialSequence))

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
# the mean is about 2 (1.945)

# Question 2: What is the type of experiment3()?
# poisson experiment with binomial random variables

# Question 3: Do the two distributions match?
# the distributions don't match, they are both similar and around the same value



