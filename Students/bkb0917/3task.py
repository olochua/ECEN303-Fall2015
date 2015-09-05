__author__ = "Bailey Barksdale"
__NetID__ = "bailey13"
__GitHubID__ = "bkb0917"

import random

Cardinality = 2
NumberTrials = 1000

TrialSequence = []
for TrialIndex in range(0, NumberTrials):
    prob = random.randrange(100)
    if prob < 75:
        TrialSequence.append(1)
    else:
        TrialSequence.append(0)




EmpiricalDistribution = []
for OutcomeIndex in range(0, Cardinality):
    EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))
print EmpiricalDistribution
