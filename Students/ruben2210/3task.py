__author__ = "Ruben Rodriguez"
__NetID__ = "ruben2210"
__GitHubID__ = "ruben2210"

import random

Cardinality = 2
NumberTrials = 1000

TrialSequence = []
for TrialIndex in range(0, NumberTrials):
    TrialSequence.append(random.randrange(Cardinality))
    #
    # EDIT
    #

EmpiricalDistribution = []
for OutcomeIndex in range(0, Cardinality):
    EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))
print EmpiricalDistribution
