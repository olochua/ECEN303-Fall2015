__author__ = "Charles Wallace"
__NetID__ = "chaswallace3"
__GitHubID__ = "chaswallace3"

import random

Cardinality = 2
NumberTrials = 1000

TrialSequence = []
for TrialIndex in range(0, NumberTrials):
        if (0 or 1 or 2) == random.randrange(4):
            TrialSequence.append(1)

        else:
            TrialSequence.append(0)
            

EmpiricalDistribution = []
for OutcomeIndex in range(0, Cardinality):
    EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))
print EmpiricalDistribution
