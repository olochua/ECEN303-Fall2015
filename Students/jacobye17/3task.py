__Author__ = "Jacoby Prestwood"
__NetID__ = "jacobye17"
__GitHubID__ = "jacobye17"

import random

Cardinality = 2
NumberTrials = 1000

TrialSequence = []
for TrialIndex in range(0, NumberTrials):
    if random.random() < .25000000:
        TrialSequence.append(0)
    else:
        TrialSequence.append(1)

EmpiricalDistribution = []
for OutcomeIndex in range(0, Cardinality):
    EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))
print EmpiricalDistribution
