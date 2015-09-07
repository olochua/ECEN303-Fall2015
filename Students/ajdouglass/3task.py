__author__ = 'Andrew Douglass'
__NetID__ = "adoulgas"
__GitHubID__ = "ajdouglass"

import random

Cardinality = 2
NumberTrials = 1000

CoinFlipBiased = [0, 1, 1, 1]  # 75% biased towards 1
TrialSequence = []
for TrialIndex in range(0, NumberTrials):
    TrialSequence.append(CoinFlipBiased[random.randrange(4)])   # choose random index from CoinFlipBiased list

EmpiricalDistribution = []
for OutcomeIndex in range(0, Cardinality):
    EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))
print(EmpiricalDistribution)
