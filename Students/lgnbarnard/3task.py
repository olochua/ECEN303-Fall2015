__author__ = "Logan Barnard"
__NetID__ = "lgn_barnard"
__GitHubID__ = "lgnbarnard"

import random

print("This program simulates flipping a biased coin 1000 times")

Cardinality = 2
NumberTrials = 1000

TrialSequence = []
#used random.random to return floating point rather than random.randrange(Cardinality)
for TrialIndex in range(0, NumberTrials):
    if random.random()<.75:
        TrialSequence.append(1)
    else:
        TrialSequence.append(0)

EmpiricalDistribution = []
for OutcomeIndex in range(0, Cardinality):
    EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))
print("[Heads, Tails]= ", EmpiricalDistribution)
