__author__ = "Jordan Lewallen"
__NetID__ = "jlewallen18"
__GitHubID__ = "jlewallen18"

import random

Cardinality = 2
NumberTrials = 1000

#number of flips

flips = 0

TrialSequence = []
for TrialIndex in range(0, NumberTrials):
    TrialSequence.append(random.randrange(Cardinality))
    if ((TrialSequence.count(1)/float(NumberTrials)) < 0.75) == True:
        TrialSequence[flips] = 1
    else:
        TrialSequence[flips] = 0
    flips = flips + 1

EmpiricalDistribution = []
for OutcomeIndex in range(0, Cardinality):
    EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))
print (EmpiricalDistribution)
