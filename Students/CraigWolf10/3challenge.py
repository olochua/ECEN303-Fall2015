__author__ = "Craig Wolf"  # EDIT
__NetID__ = "Dallascowboys10"  # EDIT
__GitHubID__ = "CraigWolf10"  # EDIT
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
import numpy as np




ParameterP = 1.0/3.0    # Parameter of digital coin
ParameterA = 1.0/3.0    # Parameter of digital coin A
ParameterB = 1.0/2.0    # Parameter of digital coin B
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
    #brv = (math.factorial(n)/((math.factorial(k)*math.factorial(n-k)))*(math.pow(p,k))*(math.pow((1-p),(n-k))))
    brv = np.random.binomial(n,p,1000)
    return brv[random.randint(0,len(brv)-1)]

    #This method returns a binomial random variable with parameters n and p.
    #The default parameters are n=1 and p=0.5; this can be changed by passing
    #arguments to the method.

    numberones = 0
    for BinomialIndex in range(0,n):
        numberones += biasedcoinflip(p)
    return numberones



def poisson(parameterpoisson=10):
    #ps = ((parameterpoisson^k)/math.factorial(k))*math.exp(-1*parameterpoisson)
    ps = np.random.poisson(parameterpoisson,1000)
    return ps[random.randint(0,len(ps)-1)]

def experiment3(parameterpoisson3=10, p=0.5):
    return binomialflips(poisson(parameterpoisson3), p)
    # return poisson(binomialflips(parameterpoisson3, p))
print "Poison:"
print poisson()

ParameterPoisson = 10
TrialSequence = []

for TrialIndex1 in range(0, NumberTrials):
    TrialSequence.append(experiment3(ParameterPoisson))
print "Mean:"
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

def experiment4(parameterpoisson3=10, p=0.5):
    return poisson(binomialflips(parameterpoisson3), p)
    # return poisson(binomialflips(parameterpoisson3, p))
print "Poison:"
print poisson()

ParameterPoisson = 10
TrialSequence = []

for TrialIndex1 in range(0, NumberTrials):
    TrialSequence.append(experiment3(ParameterPoisson))
print "Mean:"
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
plt.xlabel("Value2")
plt.ylabel("Probability2")
plt.xticks(XticksIndex, OutcomeIndex2)
plt.show()


# Question 1: What is the mean of experiment3()?
# The mean of experiment3 is most often 4 but occasionally 5.

# Question 2: What is the type of experiment3()?
# This is a binomial-poisson experiment.

# Question 3: Do the two distributions match?
# The two distributions are often similar, but they do not match.
