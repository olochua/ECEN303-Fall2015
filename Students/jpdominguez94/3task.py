__author__ = "Jose Pablo Dominguez"
__NetID__ = "jpdominguez94"
__GitHubID__ = "jpdominguez94"

import random

Cardinality = 2
NumberTrials = 1000

TrialSequence = []
for TrialIndex in range(0, NumberTrials):
    #TrialSequence.append(random.randrange(Cardinality)) NOT NEEDED
    if random.random() < .75:  #Generate random number and check the probability
        TrialSequence.append(1)
    else:                      #If it's more than .75 output a 0
        TrialSequence.append(0)

EmpiricalDistribution = []
for OutcomeIndex in range(0, Cardinality):
    EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))
print(EmpiricalDistribution)
