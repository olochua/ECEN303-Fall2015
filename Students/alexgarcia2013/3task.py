__author__ = 'Alexander Garcia'
__NetID__ = 'alexgarcia2013'
__GitHubID__ = 'alexgarcia2013'

import random   #inporting random lib

Cardinality = 2         #size of set, 2 since a coin
NumberTrials = 1000     #number of times the coin is flipped

TrialSequence = []
for TrialIndex in range(0, NumberTrials):   #from 0 to 1000 trials
    if random.random() < 0.75:              #case where prob is 75%
        TrialSequence.append(1)             #adds 1 to end of TrialSequence
else:                                       #case for zero
    TrialSequence.append(0)                 #adds 0 to end of Trial Sequence

EmpiricalDistribution = []
for OutcomeIndex in range(0, Cardinality):
    EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))
print(EmpiricalDistribution)   
