__author__ = "Madeline Kinnaird"
__NetID__ = "mrk13"
__GitHubID__ = "mkinnaird16"

import random

Cardinality = 2
NumberTrials = 1000

TrialSequence = []
for TrialIndex in range(0, NumberTrials):
    TrialSequence.append(random.randrange(Cardinality))
    
    if random.random() < .75:
        Trialsequence.append(1)
    else:
        Trialsequence.append(0)

EmpiricalDistribution = []
for OutcomeIndex in range(0, Cardinality):
    EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))
print EmpiricalDistribution
