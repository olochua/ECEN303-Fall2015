__author__ = "Seungwon Yoon"
__NetID__ = "ysw0927"
__GitHubID__ = ""

import random

Cardinality = 2
NumberTrials = 1000

def coinflip(p=0.75):
    if random.random() < p:
        return 1
    else:
        return 0;


TrialSequence = []
for TrialIndex in range(0, NumberTrials):
    TrialSequence.append(random.randrange(Cardinality))
    #
    # EDIT
    # Modify code to produce biased binary coin flip that returns one with probability 0.75
    # and zero otherwise
    #

EmpiricalDistribution = []
for OutcomeIndex in range(0, Cardinality):
    EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))
print EmpiricalDistribution
