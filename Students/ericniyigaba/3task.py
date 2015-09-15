__author__ = "Eric Niyigaba"
__NetID__ = "ericniyigaba"
__GitHubID__ = "ericniyigaba"

import random

Cardinality = 2
NumberTrials = 1000

TrialSequence = []
for TrialIndex in range(0, NumberTrials): #0 to 1000 trials
    TrialSequence.append(random.randrange(Cardinality))

    if random.random() < 0.75:  #number is generated and compared to 75 % probability
        TrialSequence.append(1)
    else:
        TrialSequence.append(0)  # generated number is greater than .75

EmpiricalDistribution = []
for OutcomeIndex in range(0, Cardinality):
    EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))
print(EmpiricalDistribution)
