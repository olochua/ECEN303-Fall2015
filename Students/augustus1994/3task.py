__author__ = "Fletcher Watts"
__NetID__ = "augustus1994"
__GitHubID__ = "augustus1994"

import random

Cardinality = 2
NumberTrials = 1000

TrialSequence = []
for TrialIndex in range(0, NumberTrials):
    if random.random() <= .75:
        TrialSequence.append(1)
    else:
        TrialSequence.append(0)
    # TrialSequence.append(random.randrange(Cardinality))
    #
    # EDIT
    # Modify code to produce biased binary coin flip that returns one with probability 0.75
    # and zero otherwise
    #

EmpiricalDistribution = []
for OutcomeIndex in range(0, Cardinality):
    EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))
print EmpiricalDistribution
