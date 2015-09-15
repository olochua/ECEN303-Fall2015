__author__ = "Weston Torti"
__NetID__ = "tort115"
__GitHubID__ = "westort"

import random

Cardinality = 2
NumberTrials = 1000

TrialSequence = []
BiasedCoin= [1,1,1,0] # setting the coin to have a 75% change return a 1(with infinite trials)
for TrialIndex in range(0, NumberTrials):
    TrialSequence.append(BiasedCoin[random.randrange(4)])

EmpiricalDistribution = []
for OutcomeIndex in range(0, Cardinality):
    EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))
print EmpiricalDistribution
