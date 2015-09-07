__author__ = "Kaitlin Basham"
__NetID__ = "klb3736"
__GitHubID__ = "klb3736"

#This code simulates a biased coin flip that returns a 1 with a
#probability of 0.75 and returns a 0 otherwise.

import random

Cardinality = 2
NumberTrials = 1000

TrialSequence = []
for TrialIndex in range(0, NumberTrials):
    if random.random() >= 0.25: TrialSequence.append(1) #return 1 with a probability of 0.75
    else: TrialSequence.append(0)                       #return 0 with a probability of 0.25

EmpiricalDistribution = []
for OutcomeIndex in range(0, Cardinality):
    EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))
print EmpiricalDistribution

