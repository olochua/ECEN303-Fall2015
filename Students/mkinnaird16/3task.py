__author__ = ""
__NetID__ = ""
__GitHubID__ = ""

import random

Cardinality = 2
NumberTrials = 1000

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
