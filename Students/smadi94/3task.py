__author__ = "Zachary Smadi"
__NetID__ = "smadi94"
__GitHubID__ = "smadi94"

import random

Cardinality = 2
NumberTrials = 1000

TrialSequence = []
for TrialIndex in range(0, NumberTrials):
    if random.random() <= 0.25:
        TrialSequence.append(0)
    else:
        TrialSequence.append(1)

EmpiricalDistribution = []
for OutcomeIndex in range(0, Cardinality):
    EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))
print EmpiricalDistribution