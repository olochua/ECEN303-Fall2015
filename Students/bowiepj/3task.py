__author__ = "Philip Bowie"
__NetID__ = "bowiepj"
__GitHubID__ = "bowiepj"

import random

Cardinality = 2
NumberTrials = 1000

TrialSequence = []
for TrialIndex in range(0, NumberTrials):
    #TrialSequence.append(random.randrange(Cardinality))
    if random.random()< .75:
        TrialSequence.append(1) #75% chance is 1
    else:
        TrialSequence.append(0) #25% chance is 0

EmpiricalDistribution = []
for OutcomeIndex in range(0, Cardinality):
    EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))
print EmpiricalDistribution
