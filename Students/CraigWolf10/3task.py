__author__ = "Craig Wolf"
__NetID__ = "Dallascowboys10"
__GitHubID__ = "CraigWolf10"

import random

Cardinality = 2
NumberTrials = 1000
TrialSequence = []
EmpiricalDistribution = []
Count = 0

for TrialIndex in range(0, NumberTrials):
    TrialSequence.append(random.randrange(Cardinality))
    if ((TrialSequence.count(1)/float(NumberTrials)) < 0.750) == True:
        TrialSequence[Count] = 1
    else:
        TrialSequence[Count] = 0
    Count = Count + 1

for OutcomeIndex in range(0, Cardinality):
    EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))
print EmpiricalDistribution
