__author__ = "Rodney Siders"
__NetID__ = "rodney6359"
__GitHubID__ = "rodney6359"

import random

Cardinality = 2
NumberTrials = 1000

TrialSequence = []
for TrialIndex in range(0, NumberTrials):
    TrialSequence.append(random.randrange(Cardinality))
    if random.random() <= 0.75:
        TrialSequence.append(1) # For when Heads 0.75
    if random.random() > 0.75:
        TrialSequence.append(0) # For when Tails is 0.25

EmpiricalDistribution = []
for OutcomeIndex in range(0, Cardinality):
    EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))
print EmpiricalDistribution
