__author__ = "Justin Lewis"
__NetID__ = "justin94lewis"
__GitHubID__ = "LewisWithoutClark"

import random

Cardinality = 2
NumberTrials = 1000

BiasedProb = 0.75

TrialSequence = []
for TrialIndex in range(0, NumberTrials):
    if random.random() <= BiasedProb:
        TrialSequence.append(1)
    else:
        TrialSequence.append(0)

EmpiricalDistribution = []
for OutcomeIndex in range(0, Cardinality):
    EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))

print EmpiricalDistribution
