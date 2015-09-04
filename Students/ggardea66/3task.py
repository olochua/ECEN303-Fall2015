__author__ = "Gissel Gardea"
__NetID__ = "gardegi059"
__GitHubID__ = "ggardea66"

import random

Cardinality = 2
NumberTrials = 1000
Coins= 2

TrialSequence = []
for TrialIndex in range(0, NumberTrials):
    TrialSequence.append(random.randrange(Cardinality))
    if random.random() < .75:
        Coins = 1
    else:
        Coins = 0
        TrialSequence.append(Coins)

EmpiricalDistribution = []
for OutcomeIndex in range(0, Cardinality):
    EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))
print EmpiricalDistribution
