__author__ = "Tyler Henderson"
__NetID__ = "tyler.henderson07"
__GitHubID__ = "thenderson37"
__SelfGrade__ = "5"
__Challenge__ = "3"

"""
Random Signals and Systems
Course: ECEN 303-502
Maximum Grade: 5
"""


import random
import math
import matplotlib.pyplot as plt
import numpy as np




ParameterP = 1/3

NumberTrials = 1000
TrialSequence = []

def biasedcoinflip(p=0.5):
    for TrialIndex in range(0, NumberTrials):
        TrialSequence.append(random.randrange(2))

        if (sum(TrialSequence)/ (1.0 *len(TrialSequence))) < ParameterP:
            TrialSequence[len(TrialSequence)-1] = 1
            return 1

        else:
            TrialSequence[len(TrialSequence)-1] = 0
            return 0

    return math.floor(random.random() + p)



def binomialflips(n=1, p=0.5):

    bernouili_RV = np.random.binomial(n,p,NumberTrials)
    return bernouili_RV[random.randint(0,len(bernouili_RV)-1)]

    #This method returns a binomial random variable with parameters n and p.
    #The default parameters are n=1 and p=0.5; this can be changed by passing
    #arguments to the method.

    Ones = 0

    for BinomialIndex in range(0,n):
        Ones += biasedcoinflip(p)
    return Ones



def poisson(parameterpoisson=10):

    ps = np.random.poisson(parameterpoisson,NumberTrials)
    return ps[random.randint(0,len(ps)-1)]

def experiment3(parameterpoisson3=10, p=0.5):
    return binomialflips(poisson(parameterpoisson3), p)

print("Poisson:")
print(poisson())

ParameterPoisson = 10
TrialSequence = []

for TrialIndex1 in range(0, NumberTrials):
    TrialSequence.append(experiment3(ParameterPoisson))

print("Mean:")
print(sum(TrialSequence)/len(TrialSequence))


Distribution = []

for OutcomeIndex1 in range(0, 21):
    Distribution.append(TrialSequence.count(OutcomeIndex1) / (1.0 * NumberTrials))

OutcomeIndex2 = range(0, 21)
num_bins = len(OutcomeIndex2)
bar_width = 0.8
XticksIndex = [(outcome + (0.5 * bar_width)) for outcome in OutcomeIndex2]
opacity = 0.4

plt.bar(OutcomeIndex2, Distribution, bar_width, alpha=opacity, color='b')
plt.title("Experiment 3")
plt.xlabel("Value")
plt.ylabel("Probability")
plt.xticks(XticksIndex, OutcomeIndex2)
plt.show()

def experiment4(parameterpoisson3=10, p=0.5):
    return poisson(binomialflips(parameterpoisson3), p)

print("Poisson:")
print(poisson())

ParameterPoisson = 10
TrialSequence = []

for TrialIndex1 in range(0, NumberTrials):
    TrialSequence.append(experiment3(ParameterPoisson))

print("Mean:")
print(sum(TrialSequence)/len(TrialSequence))

Distribution = []

for OutcomeIndex1 in range(0, 21):
    Distribution.append(TrialSequence.count(OutcomeIndex1) / (1.0 * NumberTrials))

OutcomeIndex2 = range(0, 21)
num_bins = len(OutcomeIndex2)
bar_width = 0.8
XticksIndex = [(outcome + (0.5 * bar_width)) for outcome in OutcomeIndex2]
opacity = 0.4

plt.bar(OutcomeIndex2, Distribution, bar_width, alpha=opacity, color='b')
plt.title("Experiment 4")
plt.xlabel("Value")
plt.ylabel("Probability")
plt.xticks(XticksIndex, OutcomeIndex2)
plt.show()


# Question 1: What is the mean of experiment3()?
# About 5

# Question 2: What is the type of experiment3()?
# Poisson

# Question 3: Do the two distributions match?
# They are similar but not exactly the same.
