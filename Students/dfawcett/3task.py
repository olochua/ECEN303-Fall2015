__author__ = "David Fawcett"
__NetID__ = "dgf378"
__GitHubID__ = "dfawcett"

import random

Cardinality = 2
NumberTrials = 1000

TrialSequence = []
for TrialIndex in range(0, NumberTrials):
    TrialSequence.append(random.randrange(Cardinality))
        if TrialSequence[TrialIndex] == 0:
            if random.randrange(Cardinality) == 1:
                TrialSequence[TrialIndex] =  1


EmpiricalDistribution = []
for OutcomeIndex in range(0, Cardinality):
    EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))
print EmpiricalDistribution
