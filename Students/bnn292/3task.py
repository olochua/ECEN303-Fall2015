__author__ = "Bijan Nekovei"
__NetID__ = "bnn292"
__GitHubID__ = "bnn292"

import random

Cardinality = 2
NumberTrials = 1000

TrialSequence = []
for TrialIndex in range(0, NumberTrials):
    #TrialSequence.append(random.randrange(Cardinality)) #Uneccesary line
    if random.random() < 0.75: #Change bias to 75% of winning
        TrialSequence.append(1)   # Win state (75%)
    else:
        TrialSequence.append(0)   # Failure state (25%)

EmpiricalDistribution = []
for OutcomeIndex in range(0, Cardinality):
    EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))
print(EmpiricalDistribution) #Fixed
