__author__ = "Ben Johnston"
__NetID__ = "benj626"
__GitHubID__ = "benj626"

import random

Cardinality = 2
NumberTrials = 1000

TrialSequence = []
for TrialIndex in range(0, NumberTrials):
    if random.random() < .75:
        TrialSequence.append(1)     #75% chance of success (1)
    else:
        TrialSequence.append(0)     #25% chance of failure (0)

EmpiricalDistribution = []
for OutcomeIndex in range(0, Cardinality):
    EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))
print(EmpiricalDistribution)
