__author__ = "Nirmal Patel"
__NetID__ = "nirm13ff05"
__GitHubID__ = "nirm13ff05"

import random

Cardinality = 2
NumberTrials = 1000

TrialSequence = []
for TrialIndex in range(0, NumberTrials):
    TrialSequence.append(random.randrange(Cardinality))
    if random.random() <= 0.75
        TrialSequence.append(1)
    else:
        TrialSequence.append(0)
        
EmpiricalDistribution = []
for OutcomeIndex in range(0, Cardinality):
    EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))
print EmpiricalDistribution
