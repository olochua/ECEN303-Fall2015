__author__ = "Chu Liang"
__NetID__ = "Cml1012"
__GitHubID__ = "Cml1012"

import random

Cardinality = 2
NumberTrials = 1000

TrialSequence = []
for TrialIndex in range(0, NumberTrials):
    if random.random() <= 0.75:
        TrialSequence.append(1)
    else:
        TrailSequence.append(0)

EmpiricalDistribution = []
for OutcomeIndex in range(0, Cardinality):
    EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))
print EmpiricalDistribution
