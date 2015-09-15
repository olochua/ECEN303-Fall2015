__author__ = "Trevor Malota"
__NetID__ = "TrevorMalota"
__GitHubID__ = "trevmalota"

import random

Cardinality = 2
NumberTrials = 1000

TrialSequence = []
for TrialIndex in range(0, NumberTrials):
    TrialSequence.append(random.randrange(Cardinality))
    if random.random() <= 0.75:
        TrialSequence.append(1)
    else:
        TrialSequence.append(0)


EmpiricalDistribution = []
for OutcomeIndex in range(0, Cardinality):
    EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))
print EmpiricalDistribution
