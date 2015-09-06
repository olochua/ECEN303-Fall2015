__author__ = 'benjamin'

import random

Cardinality = 4  #Noticed that this could be the denominator
NumberTrials = 1 #Setting this to one give an equal chance to select 1/(cardinality)

TrialSequence = []
for TrialIndex in range(0, NumberTrials):
    TrialSequence.append(random.randrange(Cardinality))

EmpiricalDistribution = []
for OutcomeIndex in range(0,Cardinality):
    EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))
print(EmpiricalDistribution)
#New (Adds the sections 1,2, and 3 to achieve a 3/4 or .75 chance of being "1"
EmpiricalDistribution.append(EmpiricalDistribution[0] + EmpiricalDistribution[1] + EmpiricalDistribution[2])
print(EmpiricalDistribution[4])
