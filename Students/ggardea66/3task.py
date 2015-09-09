__author__ = "Gissel Gardea"
__NetID__ = "gardegi059"
__GitHubID__ = "ggardea66"

import random

Cardinality = 2
NumberTrials = 1000
Flip= 2

TrialSequence = []
for TrialIndex in range(0, NumberTrials): #1000 trials are done
    TrialSequence.append(random.randrange(Cardinality)) 
    if random.random() < .75: #probability of 75 percent
        Flip = 1 #represents one side of the coin
    else:
        Flip = 0 #represents the other side of the coin
        TrialSequence.append(Flip) #

EmpiricalDistribution = []
for OutcomeIndex in range(0, Cardinality):
    EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))
print EmpiricalDistribution
