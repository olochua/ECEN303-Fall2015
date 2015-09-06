__author__ = Allison Badgett
__NetID__ = allisonbadgett
__GitHubID__ = allisonbadgett

import random

Cardinality = 2
NumberTrials = 1000

TrialSequence = []
for TrialIndex in range(0, NumberTrials):
    if random.random() < .75:
        TrialSequence.append(1)
    else:
        TrialSequence.append(0)

EmpiricalDistribution = []
for OutcomeIndex in range(0, Cardinality):
    EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))
print(EmpiricalDistribution) #altered original statement to work with Python 3.4
