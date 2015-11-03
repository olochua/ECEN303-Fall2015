__author__ = "Charles Wallace"
__NetID__ = "chaswallace3"
__GitHubID__ = "chaswallace3"
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


def biasedcoinflip(p=0.5):

    if(random.random()<=p):
        return 1
    else:
        return 0

    return math.floor(random.random() + p)



def binomialflips(n=1, p=0.5):

    """
    This method returns a binomial random variable with parameters n and p.
    The default parameters are n=1 and p=0.5; this can be changed by passing
    arguments to the method.
    """

    numberones=0
    for BinomialIndex in range(0,n):
        numberones += biasedcoinflip(p)
    return numberones


def poisson(parameterpoisson=10):

    return(np.random.poisson(parameterpoisson))


def experiment3(parameterpoisson3=10, p=0.5):
    return binomialflips(poisson(parameterpoisson3), p)
    # return poisson(binomialflips(parameterpoisson3, p))

def experiment4(parameterpoisson3=10, p=0.5):
    return poisson(binomialflips(parameterpoisson3, p))
    # return poisson(binomialflips(parameterpoisson3, p))


ParameterPoisson = 10
NumberTrials = 100000
TrialSequence1 = []
TrialSequence2 = []

for TrialIndex1 in range(0, NumberTrials):
    TrialSequence1.append(experiment3(ParameterPoisson))
    TrialSequence2.append(experiment4(ParameterPoisson))
print sum(TrialSequence1)/len(TrialSequence1)
print sum(TrialSequence2)/len(TrialSequence2)

Distribution1 = []
Distribution2 = []

for OutcomeIndex1 in range(0, 21):
    Distribution1.append(TrialSequence1.count(OutcomeIndex1) / (1.0 * NumberTrials))
    Distribution2.append(TrialSequence2.count(OutcomeIndex1) / (1.0 * NumberTrials))

OutcomeIndex2 = range(0, 21)
num_bins = len(OutcomeIndex2)
bar_width = 0.8
XticksIndex = [(outcome + (0.5 * bar_width)) for outcome in OutcomeIndex2]
opacity = 0.4

plt.bar(OutcomeIndex2, Distribution1, bar_width, alpha=opacity, color='b')
plt.bar(OutcomeIndex2, Distribution2, bar_width, alpha=opacity, color='g')
plt.xlabel("Value")
plt.ylabel("Probability")
plt.xticks(XticksIndex, OutcomeIndex2)
plt.show()



# Question 1: What is the mean of experiment3()?
# Answer 1: The mean of experiment 3 is most often 4, but sometimes 5

# Question 2: What is the type of experiment3()?
# Answer 2: Experiment 3 is a binomial experiment

# Question 3: Do the two distributions match?
# Answer 3: The distributions do not quite match. In the graph, the dark green color
#is where the graphs overlap. Oher than that, experiment3 is colored blue and experiment4
#is colored green

